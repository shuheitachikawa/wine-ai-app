<template>
  <div class="con">
    <div id="chartdiv"></div>
    <div id="point">
      <span id="caption">美味しい確率</span>
      <span class="display-3">{{ result }}%</span>
    </div>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'
// amChart用
import * as am4core from '@amcharts/amcharts4/core'
import * as am4charts from '@amcharts/amcharts4/charts'
import am4themes_dataviz from '@amcharts/amcharts4/themes/dataviz'
import am4themes_animated from '@amcharts/amcharts4/themes/animated'

@Component
export default class ResultChart extends Vue {
  private result = 34
  mounted() {
    this.result = 34
    /* Chart code */
    // Themes begin
    am4core.useTheme(am4themes_dataviz)
    am4core.useTheme(am4themes_animated)
    // Themes end

    // Create chart instance
    let chart = am4core.create('chartdiv', am4charts.RadarChart)
    // chart.scrollbarX = new am4core.Scrollbar()  //スクロールバー（不要なので削除）

    let data = []

    for (var i = 0; i < 20; i++) {
      data.push({ category: i, value: Math.round(Math.random() * 100) })
    }

    chart.data = data
    chart.radius = am4core.percent(100)
    chart.innerRadius = am4core.percent(50)

    // Create axes
    // let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis())
    // TS型に変更
    let categoryAxis = chart.xAxes.push(
      new am4charts.CategoryAxis<am4charts.AxisRendererCircular>()
    )
    categoryAxis.dataFields.category = 'category'
    categoryAxis.renderer.grid.template.location = 0
    categoryAxis.renderer.minGridDistance = 30
    categoryAxis.tooltip.disabled = true
    categoryAxis.renderer.minHeight = 110
    categoryAxis.renderer.grid.template.disabled = true
    //categoryAxis.renderer.labels.template.disabled = true;
    let labelTemplate = categoryAxis.renderer.labels.template
    labelTemplate.radius = am4core.percent(-60)
    labelTemplate.location = 0.5
    labelTemplate.relativeRotation = 90

    // let valueAxis = chart.yAxes.push(new am4charts.ValueAxis())
    // TS型に変更
    let valueAxis = chart.yAxes.push(
      new am4charts.ValueAxis<am4charts.AxisRendererRadial>()
    )
    valueAxis.renderer.grid.template.disabled = true
    valueAxis.renderer.labels.template.disabled = true
    valueAxis.tooltip.disabled = true

    // Create series
    let series = chart.series.push(new am4charts.RadarColumnSeries())
    series.sequencedInterpolation = true
    series.dataFields.valueY = 'value'
    series.dataFields.categoryX = 'category'
    series.columns.template.strokeWidth = 0
    series.tooltipText = '{valueY}'
    series.columns.template.radarColumn.cornerRadius = 10
    series.columns.template.radarColumn.innerCornerRadius = 0

    series.tooltip.pointerOrientation = 'vertical'

    // on hover, make corner radiuses bigger
    let hoverState = series.columns.template.radarColumn.states.create('hover')
    hoverState.properties.cornerRadius = 0
    hoverState.properties.fillOpacity = 1

    series.columns.template.adapter.add('fill', function (fill, target) {
      return chart.colors.getIndex(target.dataItem.index)
    })

    // Cursor
    chart.cursor = new am4charts.RadarCursor()
    chart.cursor.innerRadius = am4core.percent(50)
    chart.cursor.lineY.disabled = true
  }
}
</script>

<style scoped>
.con {
  position: relative;
}
#chartdiv {
  height: 450px;
}
#point {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: absolute;
  top: 230px;
  left: 50%;
  transform: translate(-50%, -50%);
}
#caption {
  display: block;
  font-size: 1rem;
}
</style>
