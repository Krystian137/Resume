document.addEventListener('DOMContentLoaded', function() {
    try {
        initializeScrollListener();
    } catch (error) {
        console.error('Error initializing app:', error);
    }
});

function initializeScrollListener() {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;

    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;

        if (currentTop < scrollPos) {
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                console.log('Scrolling up, showing nav');
                mainNav.classList.add('is-visible');
            } else {
                console.log('Scrolling down, hiding nav');
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            mainNav.classList.remove('is-visible');
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
}

document.addEventListener("DOMContentLoaded", function () {
    AOS.init({
        once: true,
        duration: 800,
        offset: 100
    });
});