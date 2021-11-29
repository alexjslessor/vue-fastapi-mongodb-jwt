<script>
import { Line, Bar } from 'vue-chartjs'

export default {
//   extends: Line,
  extends: Bar,
  props: {

    label: {
      type: String
    },

    chartdata: {
      // type: Array,
      type: Object,
      default: null
    },

    options: {
      type: Object,
      default: null
    },

    chartColors: {
      type: Object
    }

  },
  mounted () {
    this.renderChart(this.chartdata, this.options)

    // const _data = this.chartdata.map(d => d.data);
    // console.log('_data: ', _data);
    // const label = this.chartdata.map(d => d.label);
    // const _data = this.chartdata.map(list => {
    //       return list.data;
    // });
    // const _labels = this.chartdata.map(list => {
    //       return list.label;
    // });
    // console.log(_data);
    // console.log(_labels);

    // this.renderChart(
    //     {
    //       labels: _labels,
    //       datasets: [
    //         {
    //           label: this.label,
    //           data: _data,
    //           borderColor: 'magenta',
    //           // pointBorderColor: pointBorderColor,
    //           // pointBackgroundColor: pointBackgroundColor,
    //           backgroundColor: 'white'
    //         }
    //       ]
    //     },
    //     this.options
    //   );

  }
}
</script>

<!-- <script>
  import { Line } from "vue-chartjs";
  export default {
    extends: Line,
    props: {
      label: {
        type: String
      },
      chartData: {
        type: Array
      },
      options: {
        type: Object
      },
      chartColors: {
        type: Object
      }
    },
    mounted() {
      const dates = this.chartData.map(d => d.date).reverse();
      const totals = this.chartData.map(d => d.total).reverse();
  
      const {
        borderColor,
        pointBorderColor,
        pointBackgroundColor,
        backgroundColor
      } = this.chartColors;
  
      this.renderChart(
        {
          labels: dates,
          datasets: [
            {
              label: this.label,
              data: totals,
              borderColor: borderColor,
              pointBorderColor: pointBorderColor,
              pointBackgroundColor: pointBackgroundColor,
              backgroundColor: backgroundColor
            }
          ]
        },
        this.options
      );
    }
  };
  </script>
   -->

<!-- <script>
import { Line, Bar } from 'vue-chartjs'

export default {
//   extends: Line,
extends: Bar,
  props: ['chartdata', 'options'],

  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script> -->
    
<!-- <script>
import { Bar } from 'vue-chartjs'

export default {
  extends: Bar,

  data: () => ({
    chartdata: {
      labels: ['January', 'February'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#f87979',
          data: [40, 20]
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),

  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script> -->
