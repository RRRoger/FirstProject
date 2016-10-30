#!/usr/bin/env python
# -*- coding:utf-8 -*-
try:
    from DBUtils.PooledDB import PooledDB
    import pymssql
except:
    pass
from decimal import *
import datetime
import logging
# * mincached ：启动时开启的空连接数量
# * maxcached ：连接池最大可用连接数量
# * maxshared ：连接池最大可共享连接数量
# * maxconnections ：最大允许连接数量
# * blocking ：达到最大数量时是否阻塞
# * maxusage ：单个连接最大复用次数
# * setsession ：用于传递到数据库的准备会话，如 [”set name UTF-8″] 。
args = (1, 1, 1, 1, True, 0, None)
_logger = logging.getLogger()

import os
import sys

# TEXT = sys.path[0] + os.sep + 'db_config.txt'

KEYS = ['host', 'user', 'password', 'database']


class DbManager():
    def __isset(self):
        try:
            print self._con_pool
        except:
            return False
        else:
            return True

    def __init__(self, config_data):
        if not self.__isset():
            try:
                self._con_pool = PooledDB(pymssql, *args, **config_data)
            except Exception, e:
                _logger.error(u"======Exception INFO: %s" % e)
                _logger.error(u"The parameters for DBUtils is: %s" % config_data)
                print "The parameters for DBUtils is:", config_data

    def getCur(self, as_dict=True):
        try:
            self.con = self._con_pool.connection()
            cur = self.con.cursor(as_dict=as_dict)
            return cur
        except Exception, e:
            _logger.error(u'数据库连接异常%s' % e)
        return False

    def closeCur(self, cur):
        try:
            if cur:
                cur.close()
                self.con.close()
                self.con = None
        except Exception, e:
            _logger.error(u'连接关闭失败:%s' % e)

    def excuteall(self, sql, params=False, offset=False, limit=False, page_sorted_field='ID', cur=None):
        if not cur:
            cur = self.getCur()
        if offset > 1 and limit:
            sql = 'SELECT TOP ' + str(limit) + ' *  FROM (' + sql + ')y  WHERE (' + page_sorted_field + ' > \
                   (SELECT MAX(' + page_sorted_field + ') FROM(SELECT TOP ' + str(limit * (
                offset - 1)) + ' ' + page_sorted_field + '  FROM (' + sql + ')y ORDER BY ' + page_sorted_field + ' )z))  \
                   ORDER BY ' + page_sorted_field
        elif offset == 1 and limit:
            sql = 'SELECT TOP ' + str(limit) + ' *  FROM (' + sql + ')y  ORDER BY ' + page_sorted_field
        if params:
            cur.execute(sql.encode('utf-8'), params)
        else:
            cur.execute(sql.encode('utf-8'))
        resList = cur.fetchall()
        self.closeCur(cur)
        s = str(resList)
        s = s.replace('None', 'False')
        resList = eval(s)
        return {'data': resList}

    def excuteall_alter(self, sql, cur=None):
        if not cur:
            cur = self.getCur()
        cur.execute(sql.encode('utf-8'))
        return self.closeCur(cur)

    # 查询数据，其中table是表名，而columns是查询字段的集合，而constraints限定条件如：[('a','=','1'),('b','>','2')]每个tuple为与
    # offset组数limit显示多少条
    def queryall(self, table, columns, constraints=[], offset=False, limit=False, page_sorted_field=['ID'], cur=None):
        sql = u"SELECT @columns FROM @table"
        need_close = False
        if not cur:
            cur = self.getCur()
            need_close = True
        sql = sql.replace('@table', table)
        if columns and len(columns) > 0:
            sql = sql.replace('@columns', ','.join(columns))
        else:
            sql = sql.replace('@columns', '*')
        if constraints:
            sql += " where "
            for i in range(len(constraints)):
                for j in range(3):
                    if j == 2:
                        s = "'" + str(constraints[i][j]) + "'"
                    else:
                        s = constraints[i][j]
                    sql = sql + s + " "
                if i < len(constraints) - 1:
                    sql += " and "

        # 实现分页
        if offset and limit:
            num = (int(offset) - 1) * int(limit)
            page_sorted_colums = ','.join(page_sorted_field)
            sql = 'SELECT TOP ' + str(limit) + ' *  FROM ( SELECT row_number() over(order by ' + page_sorted_colums + ' ) \
             as rownumber, *  FROM (' + sql + ')S )A WHERE rownumber > ' + str(num)

        sql = sql.replace("'None'", 'NULL')
        sql = sql.replace("False", '0')
        sql = sql.replace("True", '1')
        print sql
        cur.execute(sql.encode('utf-8'))
        resList = cur.fetchall()
        s = str(resList)
        s = s.replace('None', 'False')
        resList = eval(s)
        if need_close:
            self.closeCur(cur)
        return {'data': resList}

    def update(self, sql):
        res = None
        cur = None
        try:
            cur = self.getCur()
            _logger.info(u"sql回调语句:%s" % sql)
            res = cur.execute(sql)
            self.con.commit()
        except Exception, e:
            _logger.error(u"更新失败进行回滚:%s" % e)
            self.con.rollback()
        finally:
            self.closeCur(cur)
        return res

    def insert(self, sql):
        res = None
        cur = None
        try:
            cur = self.getCur()
            res = cur.execute(sql)
            self.con.commit()
        except Exception, e:
            _logger.error(u"插入失败进行回滚:%s" % e)
            _logger.error(u"插入失败SQL:%s" % sql)
            self.con.rollback()
        finally:
            self.closeCur(cur)
        return res

    def delete(self, sql):
        res = None
        cur = None
        try:
            cur = self.getCur()
            res = cur.execute(sql)
            self.con.commit()
        except Exception, e:
            _logger.error(u"删除失败进行回滚:%s" % e)
            _logger.error(u"删除失败SQL:%s" % sql)
            self.con.rollback()
        finally:
            self.closeCur(cur)
        return res



# test

if __name__ == '__main__':
   
    sql = '''
         select 
                 ID,BillNO,Date,SupplyID,DeptID,EmpID,RowID,ItemID,UnitName,Qty,Price,Amount,TaxRate,TaxAmount,SumAmount,ToDate,WriteTime
            from T_K3_PurchaseOrder 
    '''
    sql = """
               select 
                distinct BillNO 
            from T_K3_PurchaseOrder where (ReadTime is null) or (WriteTime > ReadTime) """
    config_data = {'database': 'ZX_920', 'charset': 'utf8', 'host': '192.168.11.234', 'user': 'sa', 'password': '123',
     'port': '1433'}
    print datetime.datetime.now()
    a = DbManager(config_data)
    print a,"asdsdsd"
#     a.insert("insert into T_K3_Cust ([FNumber],[FName]) values('asd','asd')")
    # res = a.excuteall(sql,offset=1,limit=20,page_sorted_field='BillNO')
    sql = """alter table T_K3_Post add ItemLength decimal(18,2)"""

    sql = """

SELECT TOP 20 *  FROM (
            select 
                ID ID,
                FItemID k3_id,
                FNumber code,
                FName name,
                UnitName uom_name,
                StockCode stock_code,
                FSalePrice sale_price,
                FOrderPrice purchase_price,
                PP brand,
                PL category,
                Price price,
                SPJS notes,
                YZJK is_imported,
                QTTH return_in7days,
                MFAZ setup4free,
                PPBX brand_repair,
                FBarCode ean13,
                FDeleted active,
                ItemLength ItemLength,
                ItemWidth ItemWidth,
                ItemHeight ItemHeight,
                ItemWeight ItemWeight
            from T_K3_Item 
         where WriteTime > '1993-06-07 15:30:00' )y  ORDER BY ID
    """
    res = a.excuteall(sql)
    print datetime.datetime.now()
    print res
