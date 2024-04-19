<template>
    <div class="img-container">
        <img src="../assets/pawpal.png" height="80px"/>
    </div>
    <div class="view-container">
        <InputForm v-if="selected=== 'form'" @selected="updateSelected" @pet="updatePet"/>
        <SelectText v-if="selected=== 'selectText'" @selected="updateSelected" @text="updateDescription"/>
        <SelectImage v-if="selected=== 'selectImage'" @image="updateImage" @isLoading="updateIsLoading" @handleSubmit="handleSubmit"/>
        <Loading :isLoading = "isLoading"/>
        <Result v-if="selected === 'result'" :result="result" :pet="pet" :actualConfidence="actualConfidence" :shapData="shapData" @selected="updateSelected"/>
        <!-- <button @click="test">CLICK HERE</button> -->
    </div>
</template>

<script>
import axios from 'axios';
import InputForm from '../components/InputForm.vue';
import SelectText from '../components/SelectText.vue';
import SelectImage from '../components/SelectImage.vue';
import Loading from '../components/Loading.vue';
import Result from '../components/Result.vue';

export default {
    components: {
        InputForm,
        SelectText,
        SelectImage,
        Loading,
        Result,
    },
    name: 'Home',
    data() {
        return {
            pet: {},
            selected: "form",
            isLoading: false,
            sample_json : {
                "Name": "Nibble",
                "Type": "Dog",
                "Age": 3,
                "Gender": "Male",
                "Breed1": "Golden",
                "Breed2": null,
                "Colors": ["Brown", "White"],
                "MaturitySize": "Medium",
                "FurLength": "Short",
                "Vaccinated": false,
                "Dewormed": false,
                "Sterilized": false,
                "Health": "Healthy",
                "Fee": 0,
                "State": "Selangor",
                "PhotoAmt": 0,
                "VideoAmt": 0,
                "Description": "002efc654", 
                "Photo": "002efc654" 
            },
            result: {},
            actualConfidence: 0,
            shapData: {},
        }
    }, 
    methods: {
        updateSelected(selected) {
            console.log("updateselected");
            window.scrollTo({
                top: 0,
                left: 0,
                behavior: "smooth",
            });
            this.selected = selected;
        },
        updatePet(pet) {
            this.pet = pet;
        },
        updateDescription(description) {
            this.pet.Description = description;
        },
        updateImage(image) {
            this.pet.Photo = image;
        },
        updateIsLoading(isLoading) {
            this.isLoading = isLoading;
        },
        async handleSubmit() {
            try {
                const response = await axios.post('https://pet-prediction-tool-wuvjjxgjhq-as.a.run.app/upload', this.pet);
                // const response = await axios.post('http://127.0.0.1:5000/upload', this.pet);
                const temp = response.data[0];
                console.log(temp);
                this.actualConfidence = parseFloat((temp.Confidence).toFixed(3));
                this.result = response.data[0];
                this.result.Confidence = 0;
                const shapValues = response.data[1];
                const shapFeatures = response.data[2];

                let shapData = {};
                for (let i = 0; i < shapValues.length; i++) {
                    shapData[shapFeatures[i]] = shapValues[i];
                }
                this.shapData = shapData;
                window.scrollTo({
                    top: 0,
                    left: 0,
                    behavior: "smooth",
                });
                this.selected = 'result';
                this.isLoading = false;

            } catch(error) {
                console.error(error);   
            }
        },
        async test() {
            try {
                const response = await axios.post('https://pet-prediction-tool-wuvjjxgjhq-as.a.run.app/upload', this.sample_json);
                // const response = await axios.post('http://127.0.0.1:5000/upload', this.pet);
                console.log(response.data);
                const temp = response.data[0];
                console.log(temp);
                this.actualConfidence = parseFloat((temp.Confidence).toFixed(3));
                this.result = response.data[0];
                this.result.Confidence = 0;
                const shapValues = response.data[1];
                const shapFeatures = response.data[2];

                let shapData = {};
                for (let i = 0; i < shapValues.length; i++) {
                    shapData[shapFeatures[i]] = shapValues[i];
                }
                this.shapData = shapData;
                this.selected = 'result';
                this.isLoading = false;
            } catch(error) {
                console.error(error);   
            }
        }
    }
}
</script>

<style>
.view-container {
    padding: 0rem 5rem;
    margin-bottom: 2rem;
}
</style>