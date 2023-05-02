<template>
  <div>
    <h1>버튼 박스 제작</h1>
    <br>
    
    <div class="box">
      <h2>예약 페이지</h2>
      <br>
      <h3>시간 선택</h3>

      <div>
        <span v-for="(time, index) in times" :key="`time-${index}`" class="selection-box">
          <span v-on:click="flicker(time)" v-bind:class="{ 'selected': selectedTimes.includes(time)}">{{ time }}</span>
        </span>
      </div>
      
      <hr>
      <h3>
        선택 시간 : <span v-for="(time, index) in selectedTimes" :key="`selected-${index}`">{{ time }}&nbsp;&nbsp;</span>
      </h3>

    </div>
    <div>

    </div>
    <br>
    
  </div>
</template>

<script>
export default {
  name : 'ButtonBox',
  data : function() {
    return {
        selectedTimes: [],
        times: [
          "00:00","00:30","01:00","01:30","02:00","02:30","03:00","03:30","04:00","04:30",
          "05:00","05:30","06:00","06:30","07:00","07:30","08:00","08:30",
          "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
          "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
          "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
        ],
    }
  },

  methods: {
    flicker: function(time) {
      if (this.selectedTimes.includes(time)) {
        this.selectedTimes.splice(this.selectedTimes.indexOf(time), 1)
      } else {
        if (this.selectedTimes.length < 5) {
          this.selectedTimes.push(time)
        } else {
          alert('5타임까지만 신청할 수 있습니다.')
        }
      }
    }
  },

  watch: {

  }
}

</script>

<style scoped>
  .box {
    width: 600px;
    height: 300px;
    margin: auto; 
    box-shadow: 0px 5px 5px gray;
  }
  .selection-box {
    display: inline-block;
    margin-top: 3px;
    margin-bottom: 3px;
    width:12.5%;
  }
  .selected {
    background-color: skyblue;
  }
</style>