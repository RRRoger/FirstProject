# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)


def get_ignore_ids(env, item_line, obj_name, field_name, context=None):
    """
    本方法抽象出来,
    用于实现下拉搜索去重的功能,
    只需要copy到对应的对象下
    需要在对应字段的标签里添加

    context="{'de-duplication':parent.detail_ids, 'obj_name':'hs.tracker.schedule.detail', 'field_name':'product_id'}"
        其中:
            de-duplication: 是主档对应的字段
            obj_name: 该明细的对象名
            field_name: 字段名

    :param env: 环境变量
    :param item_line: 页面已经缓存的明细, 包括已经在数据库
    :param obj_name: 该明细的对象名
    :param field_name: 字段名
    :param context: ~
    :return: res 忽略的id列表
    """

    _logger.info('[*Tracker] Enhance the search function of <%s> by Roger!!' % obj_name)

    res = []
    line_obj = env[obj_name]

    def _append_ignore_ids(obj_id):
        """
        :param obj_id:
        :return:
        """
        for _line in line_obj.search([('id', '=', obj_id)]).read([field_name]):
            res.append(_line[field_name][0])

    for item in item_line:
        if item and int(item[0]) == 4:
            _append_ignore_ids(item[1])
        if item and int(item[0]) in [0, 1] and isinstance(item[2], dict):
            if item[2].get(field_name, False):
                res.append(item[2][field_name])
            else:
                _append_ignore_ids(item[1])
    return res


def get_search_args(args, env, context):
    """
    获得search 参数
    :param args:
    :param env:
    :param context:
        de-duplication:
        obj_name:
        field_name:
    :return:
    """
    if context.get('de-duplication', False) and context.get('obj_name', False) and context.get('field_name', False):
        _ignore_ids = get_ignore_ids(env, context['de-duplication'], context['obj_name'], context['field_name'])
        args.append(['id', 'not in', _ignore_ids])
    return args
