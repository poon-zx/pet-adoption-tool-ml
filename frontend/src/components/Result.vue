<template>
    <div class="result">
        <div class="prediction-container">
            <h1>Predicted Adoption Speed</h1>
            <div class="flex-center">
                <h2>{{ this.result.Result }}</h2>
                <div class="confidence-container">
                    <p>Confidence</p>
                    <RadialProgress 
                        :diameter="150"
                        :completed-steps="this.result.Confidence"
                        :total-steps="1"
                        :strokeWidth="20"
                        :innerStrokeWidth="20"
                        :animateSpeed="600"
                        :startColor="'#E55D2D'"
                        :stopColor="'#D64E1E'">
                        {{ this.actualConfidence }}</RadialProgress>
                </div>
            </div>
        </div>
        <div class="result-grid-container">
            <div class="prediction-container">
                <h1>Recommended Actions</h1>
                <div class="flex-center">
                    <ul>
                        <li v-for="action in this.result.Recommendations" :key="action">{{ action }}</li>
                    </ul>
                </div>
            </div>
            <div class="prediction-container">
                <table>
                    <thead>
                        <tr>
                        <th>Attribute</th>
                        <th>SHAP value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(value, attribute) in this.result.Shapleys" :key="attribute">
                        <td>{{ attribute }}</td>
                        <td>{{ value }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div>
            <img src="http://127.0.0.1:5000/shap_plot" alt="SHAP Values Waterfall Plot" width="100%">
        </div>
    </div>
</template>

<script>
import RadialProgress from "vue3-radial-progress";

export default {
    components: {
        RadialProgress,
    },
    props: {
        result: {
            type: Object,
            required: true
        },
        pet: {
            type: Object,
            required: true
        },
        actualConfidence: {
            type: Number,
            required: true
        }
    },
    data() {
        return {
            sample_result: {
                Result: "1 Week",
                Confidence: 0,
                Shapleys: {"FurLength": 0.221, "PhotoAmt": 0.11},
                Recommendations: ['Increase photo amount', 'Add more description', 'Don`t vaccinate'],

            },
            actualSampleConfidence: 0.6,
        }
    },
    mounted() {
        this.startUpdateConfidence();
    },
    methods: {
        startUpdateConfidence() {
            setTimeout(() => {
                this.updateConfidence();
            }, 80); 
        },
        updateConfidence() {
            console.log("updateConfidence");
            this.sample_result.Confidence = this.actualSampleConfidence;
            this.result.Confidence = this.actualConfidence;
        },
    },
};
</script>

<style>
.result h1 {
    font-size: 2em;
    text-align: center;
    color: #333;
}

.result h2 {
    margin: -20px 80px 0 0;
}

@media screen and (max-width: 768px) {
    .result h2 {
        margin: 0;
    }
}
.result p {
    font-size: 1.2em;
    text-align: center;
    color: #666;
    margin: 3px 0 0 0;
}

.flex-center {
    align-items: center;
    flex-wrap: wrap;
}

.prediction-container {
    background-color: #fffbf3;
    padding: 2rem;
    border-radius: 2rem;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    margin: 20px 0;
    align-items: center;
}

.confidence-container {
    align-items: center;
    margin-left: 30px;
}

.result {
    padding: 0rem 10rem;
}

@media screen and (max-width: 1024px) {
    .result{
        padding: 0rem 0rem;
    }
}

.vrp__inner {
    font-size: x-large !important;
}

.result-grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px 20px;
}

@media (max-width: 740px) {
    .result-grid-container {
        display: block;
    }
}

table {
    width: 100%;
    border-collapse: collapse;
    font-family: Arial, sans-serif;
  }

  th, td {
    padding: 10px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }

  th {
    background-color: #E55E2D;
    color: white;
  }

  td {
    background-color: #FCFCFC;
  }

  tr:nth-child(even) td {
    background-color: #F5F5F5;
  }
</style>