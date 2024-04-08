<template>
    <form @submit.prevent="savePet">
        <div class="grid-container-form">
            <div class="card" v-for="(d, index) in descriptions">
                <input
                v-model="selectedDescription"
                type="radio"
                :value="d.id"
                :id="`radio-${index}`"
            />
                {{ d.description }}
            </div>
        </div>
        <div class="flex-center">
            <button class="button" type="submit" :disabled="!selectedDescription">Next</button>
        </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            descriptions: [
                {id: "002efc654", description: "Seidi was rescued at Glenmaria area. She is a very gentle girl, quiet and very suitable as a companion dog. She loves to be cuddled and she loves human interactions. She is a very quiet girl hence she is not suitable as a guard dog. She is easy with food and prefers to do her business at the grass areas. Generally a very easy dog to take care and she loves car rides, and will sit quietly in the car when you drive. If you think you can provide her a good home, please contact me at Tony"},
                {id: "00d26f809", description: "Jon Snow is a stray from the University of Nottingham Malaysia Campus, and was rescued and is being fostered by UNMC students. He is a very sturdy, strong puppy with a big personality. He\'ll be a good guard dog. His adopter will need to agree to neuter him once he is old enough. We will take and hold the RM fee which will be used to pay for operation when he is old enough."},
                {id: '0162ff4ad', description: "My cat is stray cat, likes lost cat.. coz I try to find it mon, but no news... and it body all the dermatitis.. the ears most serious, so I bring it look Dr. and cure... recovery in good condition now ^^ ... and very very lively.. it also like shower.. it really special !! but I just study in Malaysia's student and next week I will go back my hometown Taiwan.. so I need someone can help and feed it... please!! Treatment Records: 22 Jan >> Weight : 1 Kg Injection: Dewormed x1 Dermatitis x1 29 Jan >> Injection: Dermatitis x1 Tetanus vaccine x1"},
                {id: "01e35d03f", description: "lovely , lovely , lovely he is manager of love company 😉 you will enjoy his friendly lovely presence better to adopt with any siblings"},
                {id: "025e61a40", description: "Tan Sri is one of the vet's favourite dogs because he is so friendly and affectionate. He is good on-leash, knows basic commands and loves attention. He currently lives with Baby, whom he plays very well with. Adoption by donation."},
                {id: "029e31937", description: "Trip was rescued from Pekeliling bus station when he was just a few months old. He had been hit by a car and his left paw was dragging on the floor. It is permanently partially paralysed, but he is still able to use it. He is a very happy, loving cat. He loves to play and then cuddle. Comes with litter tray and toys."},
            ],
            selectedDescription: null,
        }
    },
    methods: {
        savePet() {
            if (!this.selectedDescription) {
                alert("Please select a description.");
                return;
            }
            this.$emit("text", this.selectedDescription);
            this.$emit("selected", "selectImage");
            console.log(this.selectedDescription);
        }
    },
    emits: ['text', 'selected'],
}
</script>

<style>
.card {
    border-radius: 10px;
    padding: 1rem;
    margin: 10px;
    background-color: #fffbf3;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: all 0.3s;
    display: flex;
    align-items: center;
}

.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-gap: 20px 20px;
}

@media (max-width: 1024px) {
    .grid-container {
        display: block; 
    }
}

.view-container {
    padding: 2rem 5rem;
}

input[type="radio"] {
  width: 20px;
  height: 20px;
  margin-right: 10px;
  accent-color: #e55e2d;
  cursor: pointer;
}

</style>