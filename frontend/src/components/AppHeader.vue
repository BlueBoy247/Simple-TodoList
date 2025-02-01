<template>
<header>
    <img src="@/assets/logo.png" alt="Logo" />
    <div>
        <h1>{{ title }}</h1>
        <p>Copyright &copy; {{ year }} {{ author }}</p>
    </div>
</header>
</template>

<script>
export default{
    name: 'AppHeader',
    props: {
        title: String,
        author: String,
        year: String
    }
}
</script>

<style scoped>
header{
    display: flex;
    justify-content: center;
    align-items: center;
}
img{
    width: 70px;
    height: 70px;
    margin-right: 10px;
}
div{
    margin-left: 10px;
    text-align: center;
}
</style>