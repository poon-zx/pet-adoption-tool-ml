<template>
    <form @submit.prevent="savePet">
        <div class="grid-container">
            <div class="card" v-for="(i, index) in images">
                <input
                v-model="selectedImage"
                type="radio"
                :value="i.id"
                :id="`radio-${index}`"
                required
            />
                <img :src="i.imgUrl" alt="pet" height="200px"/>
            </div>
        </div>
        <div class="flex-center">
            <button class="button" type="submit" :disabled="!selectedImage">Next</button>
        </div>
    </form>
</template>

<script>
export default {
    data() {
        return {
            images: [ 
                {id: "029e31937", imgUrl: "./029e31937.jpg"},
                {id: "025e61a40", imgUrl: "./025e61a40.jpg"},
                {id: "0162ff4ad", imgUrl: "./0162ff4ad.jpg"},
                {id: "01e35d03f", imgUrl: "./01e35d03f.jpg"},
                {id: "00d26f809", imgUrl: "./00d26f809.jpg"},
                {id: "002efc654", imgUrl: "./002efc654.jpg"},
            ],
            selectedImage: null,
        }
    },
    methods: {
        savePet() {
            if (!this.selectedImage) {
                alert("Please select an image.");
                return;
            }
            this.$emit("image", this.selectedImage);
            this.$emit("isLoading", true);
            this.$emit("handleSubmit");
            console.log(this.selectedImage);
        }
    },
    emits: ['image', 'isLoading', 'handleSubmit'],
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
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 20px 20px;
}

@media (max-width: 1024px) {
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
    }
}

@media (max-width: 740px) {
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