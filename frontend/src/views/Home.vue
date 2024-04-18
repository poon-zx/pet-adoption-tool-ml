<template>
    <div class="img-container">
        <img src="../assets/pawpal.png" height="80px"/>
    </div>
    <div class="view-container">
        <InputForm v-if="selected=== 'form'" @selected="updateSelected" @pet="updatePet"/>
        <SelectText v-if="selected=== 'selectText'" @selected="updateSelected" @text="updateDescription"/>
        <SelectImage v-if="selected=== 'selectImage'" @image="updateImage" @isLoading="updateIsLoading" @handleSubmit="handleSubmit"/>
        <Loading :isLoading = "isLoading"/>
        <Result v-if="selected === 'result'" :result="result" :pet="pet" :actualConfidence="actualConfidence"/>
        <button @click="test">CLICK HERE</button>
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
                "FurLength": "Long",
                "Vaccinated": true,
                "Dewormed": false,
                "Sterilized": false,
                "Health": "Healthy",
                "Fee": 0,
                "State": "Selangor",
                "PhotoAmt": 1,
                "VideoAmt": 1,
                "Description": "002efc654", 
                "Photo": "002efc654" 
            },
            result: {},
            actualConfidence: 0
        }
    }, 
    methods: {
        updateSelected(selected) {
            console.log("updateselected");
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
                const response = await axios.post('http://127.0.0.1:5000/upload', this.pet);
                this.selected = 'result';
                console.log(this.selected);
                this.isLoading = false;
                console.log(response.data[0]);
                const temp = response.data[0];
                this.actualConfidence = temp.Confidence;
                this.result = response.data[0];
                this.result.Confidence = 0;
            } catch(error) {
                console.error(error);   
            }
        },
        async test() {
            try {
                const response = await axios.post('http://127.0.0.1:5000/upload', this.sample_json);
                this.isLoading = false;
                this.selected == 'result';
                console.log(response.data[0]);
                const temp = response.data[0];
                this.actualConfidence = temp.Confidence;
                this.result = response.data[0];
                this.result.Confidence = 0;
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