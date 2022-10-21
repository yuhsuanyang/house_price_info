<template></template>
<script>
export default{

  async getItems(clusterId){
    response = await this.$http.get('http://127.0.0.1:8000/api/' + clusterId);
  };
  created(){
    getItems(this.$route.params.clusterId);
  }
};
</script>
