<template>
  <div>
    <div class="outer">
      <div class="inner">
        <div class="row g-3 align-items-center">
          <div class="col-auto">
            <input
              type="text"
              @input="searchInput"
              @keyup.enter="onSearchEnter"
              class="form-control"
              placeholder="Search"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieSearch",
  methods: {
    searchInput(event) {
      const searchKeyword = event.target.value.trim();
      if (searchKeyword) {
        this.$emit("text-input", searchKeyword);
      }
    },
    onSearchEnter(event) {
      const search = event.target.value.trim();
      if (!search) {
        alert("검색어를 입력해주세요!");
        return;
      }
      this.$emit("search-text", search);
      event.target.value = "";
    },
  },
  computed: {
    checkLogin() {
      return this.$store.getters.checkLogin;
    },
  },
};
</script>

<style>
.outer {
  display: flex;
}

.inner {
  margin: 0 auto;
}
</style>