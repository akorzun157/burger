const dishesItems = document.querySelector('.dishes-items');

dishesItems.addEventListener('wheel', (e) => {
    e.preventDefault(); // Предотвращаем прокрутку страницы
    dishesItems.scrollBy({
        top: e.deltaY < 0 ? -100 : 100, // Прокрутка вверх или вниз
        //behavior: 'smooth' // Плавная прокрутка
    });
});