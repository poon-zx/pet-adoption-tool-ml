<template>
    <div class="loading-container" v-if="isLoading">
      <div class="loading-spinner">
        <div class="dot1"></div>
        <div class="dot2"></div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      isLoading: {
        type: Boolean,
        required: true
      },
    }
  }
  </script>
  
  <style scoped>
  .loading-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(231, 228, 228, 0.8);
    opacity: 70%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 9999;
  }
  
  .loading-spinner {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .dot1, .dot2 {
    width: 12px;
    height: 12px;
    background-color: #e55e2d;
    border-radius: 50%;
    margin: 0 5px;
    animation: bounce 1.2s infinite ease-in-out;
  }
  
  .dot2 {
    animation-delay: -0.6s;
  }
  
  @keyframes bounce {
    0%, 100% { transform: scale(0); }
    50% { transform: scale(1); }
  }
  
  .loading-text {
    margin-left: 10px;
    font-size: 16px;
    font-weight: bold;
  }
  </style>