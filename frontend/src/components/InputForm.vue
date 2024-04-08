<template>
    <form class="input-form" @submit.prevent="savePet">
        <div class="grid-container-form">
            <div class="text-field">
                <label for="name">Name</label>
                <input v-model="pet.Name" type="text" id="name" name="name" required :class="pet.Name ? '' : 'input-false'"/>
            </div>
            <div class="flex">
                <div class="age-field">
                    <label for="age">Age</label>
                    <input v-model="pet.Age" type="number" id="age" name="age" min="0" required :class="pet.Age ? '' : 'input-false'"/>
                </div>
                <div class="gender-field">
                    <label for="gender">Gender</label>
                    <multiselect v-model="pet.Gender" :options="genderOptions" id="gender" name="gender" required></multiselect>
                </div>
            </div>
            <div class="flex">
                <div class="state-field">
                    <label for="state">State</label>
                    <multiselect v-model="pet.State" :options="stateOptions" id="state" name="state"></multiselect>
                </div>
                <div class="type-field">
                    <label for="type">Type</label>
                    <multiselect v-model="pet.Type" :options="typeOptions" id="type" name="type"></multiselect>
                </div>
            </div>
            <div class="color-field">
                <label for="colors">Colors</label>
                <multiselect v-model="pet.Colors" 
                    :options="colorOptions"
                    :multiple="true"
                    :close-on-select="false"
                    :max="3"
                    id="colors"
                    name="colors">
                </multiselect>
            </div>
            <div>
                <label for="primary-breed">Primary Breed</label>
                <input v-model="pet.Breed1" type="text" id="primary-breed" name="primary-breed" required :class="pet.Breed1 ? '' : 'input-false'">
            </div>
            <div>
                <label for="secondary-breed">Secondary Breed</label>
                <input v-model="pet.Breed2" type="text" id="secondary-breed" name="secondary-breed">
            </div>
            <div>
                <span>Health Information</span>
                <div class="health-information">
                    <div class="info-container">
                        <input v-model="pet.Vaccinated" type="checkbox" id="vaccinated" /><span>Vaccinated</span>
                    </div>
                    <div class="info-container">
                        <input v-model="pet.Dewormed" type="checkbox" id="dewormed"/><span>Dewormed</span>
                    </div>
                    <div class="info-container">
                        <input v-model="pet.Sterilized" type="checkbox" id="sterilized"/><span>Sterilized</span>
                    </div>
                </div>
            </div>
            <div class="health-field">
                <label for="health-condition">Health Condition</label>
                <multiselect v-model="pet.Health" :options="healthOptions" id="health-condition" open-direction="below"></multiselect>
            </div>
            <div class="flex">
                <div class="fur-field">
                    <label for="fur">Fur Length</label>
                    <multiselect v-model="pet.FurLength" :options="furOptions" id="fur" name="fur" open-direction="below"></multiselect>
                </div>
                <div class="size-field">
                    <label for="size">Size</label>
                    <multiselect v-model="pet.MaturitySize" :options="sizeOptions" id="size" name="size" open-direction="below"></multiselect>
                </div>
            </div>
            <div class="flex">
                <div class="photo-field">
                    <label for="photo-amount">Photo Amount</label>
                    <input v-model="pet.PhotoAmt" type="number" id="photo-amount" name="photo-amount" min="0" required :class="pet.PhotoAmt ? '' : 'input-false'">
                </div>
                <div class="video-field">
                    <label for="video-amount">Video Amount</label>
                    <input v-model="pet.VideoAmt" type="number" id="video-amount" name="video-amount" min="0" required :class="pet.VideoAmt ? '' : 'input-false'">
                </div>
            </div>
        </div>
        <div class="flex-center">
            <div class="fee-container">
                <label for="fee">Fee</label>
                <input v-model="pet.Fee" type="number" id="fee" name="fee" min="0" :class="pet.Fee ? '' : 'input-false'">
            </div>
        </div>
    <div class="flex-center">
        <button class="button" type="submit">Next</button>
    </div>
    </form>
</template>

<script>
import Multiselect from 'vue-multiselect'
export default {
    components: {
        Multiselect,
    },
    data() {
        return {
            pet: {
                Name: null,
                Age: null,
                Gender: null,
                State: null,
                Type: null,
                Colors: [],
                Breed1: null,
                Breed2: null,
                Vaccinated: false,
                Dewormed: false,
                Sterilized: false,
                Health: null,
                FurLength: null,
                MaturitySize: null,
                PhotoAmt: null,
                VideoAmt: null,
                Fee: null,
            },
            genderOptions: ['Female', 'Male'],
            colorOptions: ['Black', 'Brown', 'Golden', 'Yellow', 'Cream', 'Gray', 'White'],
            stateOptions: ['Johor', 'Kedah', 'Kelantan', 'Kuala Lumpur', 'Labuan', 'Melaka', 'Negeri Sembilan', 'Pahang', 'Perak', 'Perlis', 'Pulau Pinang', 'Sabah', 'Sarawak', 'Selanggor', 'Terengganu'],
            typeOptions: ['Dog', 'Cat'],
            healthOptions: ['Healthy', 'Minor Injury', 'Serious Injury'],
            furOptions: ['Short', 'Medium', 'Long'],
            sizeOptions: ['Small', 'Medium', 'Large', 'Extra Large'],
        }
    },
    methods: {
        savePet() {
            console.log(this.pet);
            this.$emit("pet", this.pet);
            this.$emit("selected", "selectText");
        },
        getBorderColor(props) {
            if (props === 'Colors') {
                return this.pet[props].length ? '#e8e8e8' : '#E55E2D';
            }
            return this.pet[props] ? '#e8e8e8' : '#E55E2D';
        }
    },
    emits: ['pet', 'selected'],
}
</script>

<style>
.input-form {
    background-color: #fffbf3;
    padding: 2rem;
    border-radius: 2rem;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}

.img-container {
    display: flex;
    justify-content: center;
    margin: 1rem 0;
}
input {
    width: calc(100% - 11px);
    padding-left: 10px;
    border: 1px solid #e8e8e8;
    border-radius: 5px;
    height: 35px;
}

.input-false {
    border: 1px solid #E55E2D;
}
.grid-container-form {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px 50px;
}

@media (max-width: 1024px) {
    .grid-container-form {
        display: block; 
    }
}


.state-field, .type-field, .fur-length-field, .size-field, .photo-field, .video-field, .age-field, .gender-field {
    width: 48%;
}
.flex {
    display: flex;
    justify-content: space-between;
}
.flex-center {
    display: flex;
    justify-content: center;
}
input[type="checkbox"] {
    width:auto;
    margin: 0px 15px 0px 0px;
}

.health-information {
    display: flex;
    justify-content: left;
}

@media (max-width: 1024px) {
    .health-information {
        display: block;
    }
}

.info-container {
    align-items: center;
    display: flex;
    margin-right: 15px;
    background-color: #FFCF7B;
    padding: 0px 30px 0px 20px;
    border-radius: 10px;
    margin-top: 5px;
}

@media (max-width: 1024px) {
    .info-container {
        width: 40%;
    }
}

.fee-container {
    margin-top: 20px;
    width: 20rem;
    align-items: center;
    text-align: center;
}

.gender-field .multiselect__tags {
  border: 1px solid v-bind(getBorderColor('Gender')) !important;
}

.state-field .multiselect__tags {
  border: 1px solid v-bind(getBorderColor('State')) !important;
}

.type-field .multiselect__tags {
  border: 1px solid v-bind(getBorderColor('Type')) !important;
}

.color-field .multiselect__tags {
  border: 1px solid v-bind(getBorderColor('Colors')) !important;
}

.health-field .multiselect__tags {
  border: 1px solid v-bind(getBorderColor('Health')) !important;
}

.fur-field .multiselect__tags {
  border: 1px solid v-bind(getBorderColor('FurLength')) !important;
}

.size-field .multiselect__tags {
  border: 1px solid v-bind(getBorderColor('MaturitySize')) !important;
}

.multiselect__tag {
    background: #FFCF7B !important;
    color: black !important;
}

.multiselect__tag-icon:after {
  color: rgba(60, 60, 60, 0.5) !important;
}


.multiselect__tag-icon:focus:after,
.multiselect__tag-icon:hover:after {
  color: red !important;
}

#vaccinated, #dewormed, #sterilized {
    accent-color: #E55E2D;
    cursor: pointer;
}

.button {
    background-color: #E55E2D;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    margin-top: 20px;
    border: none;
}

.button:hover {
    background-color: #c14619;
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>