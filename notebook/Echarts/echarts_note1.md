# Echarts Note

## 1. Echarts图表之formatter用法

### a. 字符串模板

- 折线（区域）图、柱状（条形）图、K线图: {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
- 散点图（气泡）图 : {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
- 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
- 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）



### b. 回调函数

- 回调函数格式：

  - ```javascript
    (params: Object|Array, ticket: string, callback: (ticket: string, html: string)) => string
    ```

- ```javascript
  tooltip: {
      trigger:'item',
      padding:[20,10,20,10],
      formatter:'{a} </br>{b}:{c}%'
  },
  ```

- 

## 2. 显示下载按钮

- in variant `option`

- ```javascript
  toolbox: {
      //show: true,
      itemSize: 20,
      itemGap: 30,
      right: 50,
      feature: {
          dataView: {show:true},  // 显示数据视图
          saveAsImage: {
              //excludeComponents :['toolbox'],
              pixelRatio: 2
          }
      }
  }
  ```

- 

