<template>
    <div class="img-container">
        <img src="../assets/pawpal.png" height="80px"/>
    </div>
    <div class="view-container">
        <InputForm v-if="selected=== 'form'" @selected="updateSelected" @pet="updatePet"/>
        <SelectText v-if="selected=== 'selectText'" @selected="updateSelected" @text="updateDescription"/>
        <SelectImage v-if="selected=== 'selectImage'" @image="updateImage" @isLoading="updateIsLoading" @handleSubmit="handleSubmit"/>
        <Loading :isLoading = "isLoading"/>
        <Result v-if="selected === 'result'" :result="result" :pet="pet"/>
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
            selected: "result",
            isLoading: false,
            sample_json: {
                Name: "Nibble",
                Type: "Dog",
                Age: 3,
                Gender: "Male",
                Breed1: "Golden",
                Breed2: null,
                Colors: ["Blue", "Green"],
                MaturitySize: "Medium",
                FurLength: "Long",
                Vaccinated: true,
                Dewormed: false,
                Sterilized: false,
                Health: "Healthy",
                Fee: 0,
                State: "Selangor",
                PhotoAmt: 1,
                VideoAmt: 1,
                Description: "3aa",
                Photo: "2aa"
            },
            result: {},
            sample_result: {
                Result: "1 Week",
                Confidence: 0.8,
                Pet: ['Don`t sterilize', 'Don`t deworm', 'Don`t vaccinate'],
                Image: ['Increase photo amount', 'Increase video amount'],
                Description: ['Add more description']
            }
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
                console.log(response.data);
            } catch(error) {
                console.error(error);   
            }
        },
        async test() {
            try {
                const response = await axios.post('http://127.0.0.1:5000/upload', this.sample_json);
                console.log(response.data);
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