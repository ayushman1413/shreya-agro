document.addEventListener('DOMContentLoaded', function () {
    // Mobile nav toggle
    var navToggle = document.getElementById('navToggle');
    var mainNav = document.getElementById('mainNav');
    if (navToggle && mainNav) {
        navToggle.addEventListener('click', function () {
            mainNav.classList.toggle('open');
            var expanded = mainNav.classList.contains('open');
            navToggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
        });
    }

    // Chatbot toggle
    var chatbotToggle = document.getElementById('chatbotToggle');
    var chatbotPanel = document.getElementById('chatbotPanel');
    if (chatbotToggle && chatbotPanel) {
        chatbotToggle.addEventListener('click', function () {
            chatbotPanel.classList.toggle('open');
        });
    }

    // Search toggle -> jump to products page with focus on search
    var searchToggle = document.getElementById('searchToggle');
    if (searchToggle) {
        searchToggle.addEventListener('click', function () {
            window.location.href = '/products/#search';
        });
    }

    // Product enquiry modal
    var overlay = document.getElementById('enquiryModalOverlay');
    var closeBtn = document.getElementById('enquiryModalClose');
    var productLabel = document.getElementById('enquiryProductLabel');
    var productNameEl = document.getElementById('enquiryProductName');
    var productIdEl = document.getElementById('enquiryProductId');
    var enquiryTypeEl = document.getElementById('enquiryType');
    var formWrap = document.getElementById('enquiryFormWrap');
    var successEl = document.getElementById('enquirySuccess');
    var form = document.getElementById('enquiryForm');

    function openModal(productId, productName, enquiryType) {
        if (!overlay) return;
        formWrap.style.display = 'block';
        successEl.style.display = 'none';
        form.reset();

        if (productName) {
            productLabel.style.display = 'block';
            productNameEl.textContent = productName;
            productIdEl.value = productId || '';
            enquiryTypeEl.value = enquiryType || 'Product Enquiry';
        } else {
            productLabel.style.display = 'none';
            productIdEl.value = '';
            enquiryTypeEl.value = enquiryType || 'General Enquiry';
        }
        overlay.classList.add('open');
    }

    document.querySelectorAll('.js-open-enquiry').forEach(function (el) {
        el.addEventListener('click', function (e) {
            e.preventDefault();
            var productId = el.getAttribute('data-product-id');
            var productName = el.getAttribute('data-product-name');
            var enquiryType = el.getAttribute('data-enquiry-type') || 'Product Enquiry';
            openModal(productId, productName, enquiryType);
        });
    });

    if (closeBtn) {
        closeBtn.addEventListener('click', function () {
            overlay.classList.remove('open');
        });
    }
    if (overlay) {
        overlay.addEventListener('click', function (e) {
            if (e.target === overlay) overlay.classList.remove('open');
        });
    }

    if (form) {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            var submitBtn = form.querySelector('button[type="submit"]');
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';

            fetch(form.action, { method: 'POST', body: new FormData(form) })
                .then(function (res) { return res.json(); })
                .then(function (data) {
                    submitBtn.disabled = false;
                    submitBtn.textContent = 'Send Enquiry';
                    if (data.success) {
                        formWrap.style.display = 'none';
                        successEl.style.display = 'block';
                    } else {
                        alert(data.message || 'Something went wrong. Please try again.');
                    }
                })
                .catch(function () {
                    submitBtn.disabled = false;
                    submitBtn.textContent = 'Send Enquiry';
                    alert('Network error. Please try again.');
                });
        });
    }

    // Product listing: client-side search + category filter (progressive enhancement;
    // the same filtering also works server-side via ?search= and ?category= for crawlers)
    var searchInput = document.getElementById('productSearchInput');
    if (searchInput) {
        searchInput.addEventListener('input', function () {
            var term = searchInput.value.toLowerCase();
            document.querySelectorAll('[data-product-name]').forEach(function (card) {
                var name = card.getAttribute('data-product-name').toLowerCase();
                card.closest('.product-card').style.display = name.indexOf(term) > -1 ? '' : 'none';
            });
        });
    }
});
