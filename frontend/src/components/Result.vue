<template>
    <div class="result">
        <div class="prediction-container">
            <h1>Predicted Adoption Speed</h1>
            <div class="flex-center">
                <h2>{{ sample_result.Result }}</h2>
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
        <div class="prediction-container">
            <h1>Recommended Actions</h1>
            <div class="flex-center">
                <ul>
                    <li v-for="action in result.Recommendations" :key="action">{{ action }}</li>
                </ul>
            </div>
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
                Pet: ['Don`t sterilize', 'Don`t deworm', 'Don`t vaccinate'],
                Image: ['Increase photo amount', 'Increase video amount'],
                Description: ['Add more description']
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
    /* margin: 0 200px; */
    margin: 20px 0;
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
/* .arrow {
    z-index: 999;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-75%, -100%);
}

@media screen and (max-width: 768px) {
    .arrow {
        transform: translate(-27%, -100%);
    }
}

@media screen and (max-width: 620px) {
    .arrow {
        transform: translate(-27%, -60%);
    }
}

@media screen and (max-width: 588px) {
    .arrow {
        transform: translate(-44%, -25%);
    }
} */


</style>