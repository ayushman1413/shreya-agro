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

    // Chatbot logic
    var chatbotToggle = document.getElementById('chatbotToggle');
    var chatbotPanel = document.getElementById('chatbotPanel');
    var chatCloseBtn = document.getElementById('chatCloseBtn');
    var chatBody = document.getElementById('chatBody');
    var chatInput = document.getElementById('chatInput');
    var chatSendBtn = document.getElementById('chatSendBtn');

    if (chatbotToggle && chatbotPanel) {
        chatbotToggle.addEventListener('click', function () {
            chatbotPanel.classList.toggle('open');
        });
    }

    if (chatCloseBtn) {
        chatCloseBtn.addEventListener('click', function () {
            chatbotPanel.classList.remove('open');
        });
    }

    if (chatSendBtn && chatInput && chatBody) {
        function sendMessage() {
            var text = chatInput.value.trim();
            if (!text) return;

            // Add user message
            var userMsg = document.createElement('div');
            userMsg.className = 'chat-message user';
            userMsg.innerHTML = '<div class="msg-bubble">' + text + '</div>';
            chatBody.appendChild(userMsg);
            chatInput.value = '';

            // Scroll to bottom
            chatBody.scrollTop = chatBody.scrollHeight;

            // Show thinking
            var thinkingMsg = document.createElement('div');
            thinkingMsg.className = 'chat-message bot thinking-wrapper';
            thinkingMsg.innerHTML = '<div class="msg-avatar">🤖</div><div class="msg-bubble"><div class="thinking-dots"><span></span><span></span><span></span></div></div>';
            chatBody.appendChild(thinkingMsg);
            chatBody.scrollTop = chatBody.scrollHeight;

            // Fake reply after 1.5s
            setTimeout(function () {
                thinkingMsg.remove();
                var botMsg = document.createElement('div');
                botMsg.className = 'chat-message bot';
                botMsg.innerHTML = '<div class="msg-avatar">🤖</div><div class="msg-bubble">Thanks for your message! As an AI, I am still learning. A human team member will contact you soon!</div>';
                chatBody.appendChild(botMsg);
                chatBody.scrollTop = chatBody.scrollHeight;
            }, 1500);
        }

        chatSendBtn.addEventListener('click', sendMessage);
        chatInput.addEventListener('keypress', function (e) {
            if (e.key === 'Enter') sendMessage();
        });
    }

    // Search toggle -> jump to products page with focus on search
    var searchToggle = document.getElementById('searchToggle');
    if (searchToggle) {
        searchToggle.addEventListener('click', function () {
            window.location.href = '/products/#search';
        });
    }

    // ---------- Product enquiry modal ----------
    var overlay = document.getElementById('enquiryModalOverlay');
    var modalBox = document.getElementById('enquiryModalBox');
    var closeBtn = document.getElementById('enquiryModalClose');
    var productPanel = document.getElementById('enquiryProductPanel');
    var productImageEl = document.getElementById('enquiryProductImage');
    var productTitleEl = document.getElementById('enquiryProductTitle');
    var productDescEl = document.getElementById('enquiryProductDesc');
    var packSizesWrap = document.getElementById('enquiryPackSizesWrap');
    var packSizesEl = document.getElementById('enquiryPackSizes');
    var productIdEl = document.getElementById('enquiryProductId');
    var enquiryTypeEl = document.getElementById('enquiryType');
    var formWrap = document.getElementById('enquiryFormWrap');
    var successEl = document.getElementById('enquirySuccess');
    var form = document.getElementById('enquiryForm');

    function openModal(el, productId, productName, enquiryType) {
        if (!overlay) return;
        formWrap.style.display = 'block';
        successEl.style.display = 'none';
        form.reset();

        var productImage = el.getAttribute('data-product-image');

        if (productName && productImage) {
            productPanel.style.display = 'block';
            modalBox.classList.remove('no-product-panel');
            productImageEl.src = productImage;
            productImageEl.alt = productName;
            productTitleEl.textContent = productName;
            productDescEl.textContent = el.getAttribute('data-product-desc') || '';

            var packSizes = (el.getAttribute('data-pack-sizes') || '').split(',').map(function (s) { return s.trim(); }).filter(Boolean);
            if (packSizes.length) {
                packSizesWrap.style.display = 'block';
                packSizesEl.innerHTML = '';
                packSizes.forEach(function (size) {
                    var span = document.createElement('span');
                    span.textContent = size;
                    packSizesEl.appendChild(span);
                });
            } else {
                packSizesWrap.style.display = 'none';
            }

            productIdEl.value = productId || productName;
            enquiryTypeEl.value = enquiryType || 'Product Enquiry';
        } else {
            productPanel.style.display = 'none';
            modalBox.classList.add('no-product-panel');
            productIdEl.value = productName || '';
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
            openModal(el, productId, productName, enquiryType);
        });
    });

    if (closeBtn) {
        closeBtn.addEventListener('click', function () { overlay.classList.remove('open'); });
    }
    if (overlay) {
        overlay.addEventListener('click', function (e) {
            if (e.target === overlay) overlay.classList.remove('open');
        });
    }

    // ---------- Static form submission (Web3Forms) ----------
    // No backend/database on this static build: forms POST straight to Web3Forms,
    // a free service that emails submissions to SITE_EMAIL. Get a free access key
    // at https://web3forms.com (no signup, just verify your email) and paste it
    // into every hidden "access_key" input below.
    function wireForm(formEl, wrapEl, successEl) {
        if (!formEl) return;
        formEl.addEventListener('submit', function (e) {
            e.preventDefault();
            var submitBtn = formEl.querySelector('button[type="submit"]');
            var originalText = submitBtn.textContent;
            submitBtn.disabled = true;
            submitBtn.textContent = 'Sending...';

            fetch('https://api.web3forms.com/submit', {
                method: 'POST',
                body: new FormData(formEl)
            })
                .then(function (res) { return res.json(); })
                .then(function (data) {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalText;
                    if (data.success) {
                        wrapEl.style.display = 'none';
                        successEl.style.display = 'block';
                    } else {
                        alert(data.message || 'Something went wrong. Please try again.');
                    }
                })
                .catch(function () {
                    submitBtn.disabled = false;
                    submitBtn.textContent = originalText;
                    alert('Network error. Please try again, or contact us directly by phone/email.');
                });
        });
    }

    wireForm(form, formWrap, successEl);
    wireForm(document.getElementById('generalEnquiryForm'), document.getElementById('generalFormWrap'), document.getElementById('generalFormSuccess'));
    wireForm(document.getElementById('generalModalForm'), document.getElementById('generalModalFormWrap'), document.getElementById('generalModalSuccess'));
    wireForm(document.getElementById('applicationForm'), document.getElementById('applicationFormWrap'), document.getElementById('applicationSuccess'));

    // ---------- General enquiry modal (Contact page CTAs) ----------
    var genOverlay = document.getElementById('generalEnquiryOverlay');
    if (genOverlay) {
        document.querySelectorAll('.js-open-general-enquiry').forEach(function (btn) {
            btn.addEventListener('click', function () {
                document.getElementById('generalModalType').value = btn.getAttribute('data-enquiry-type') || 'Business Partnership';
                genOverlay.classList.add('open');
            });
        });
        document.getElementById('generalEnquiryClose').addEventListener('click', function () { genOverlay.classList.remove('open'); });
        genOverlay.addEventListener('click', function (e) { if (e.target === genOverlay) genOverlay.classList.remove('open'); });
    }

    // ---------- Career application modal (Contact page) ----------
    var appOverlay = document.getElementById('applicationOverlay');
    if (appOverlay) {
        document.querySelectorAll('.js-open-application').forEach(function (btn) {
            btn.addEventListener('click', function () {
                document.getElementById('applicationPosition').textContent = btn.getAttribute('data-position') || '';
                document.getElementById('applicationPositionTitle').value = btn.getAttribute('data-position') || '';
                appOverlay.classList.add('open');
            });
        });
        document.getElementById('applicationClose').addEventListener('click', function () { appOverlay.classList.remove('open'); });
        appOverlay.addEventListener('click', function (e) { if (e.target === appOverlay) appOverlay.classList.remove('open'); });
    }

    // Preset the enquiry type dropdown from ?enquiry=... in the URL (Contact page)
    var typeSelect = document.getElementById('g_type');
    if (typeSelect) {
        var params = new URLSearchParams(window.location.search);
        var preset = params.get('enquiry');
        if (preset) typeSelect.value = preset;
    }

    // ---------- Product listing: client-side search + category filter ----------
    // Fully static: all product cards are already in the HTML; this just shows/hides them.
    var searchInput = document.getElementById('productSearchInput');
    var categoryChips = document.querySelectorAll('.filter-chips a[data-category]');
    var productCards = document.querySelectorAll('.product-grid .product-card[data-category]');

    function applyProductFilters() {
        var term = searchInput ? searchInput.value.toLowerCase() : '';
        var activeChip = document.querySelector('.filter-chips a.active');
        var category = activeChip ? activeChip.getAttribute('data-category') : 'all';

        productCards.forEach(function (card) {
            var name = (card.getAttribute('data-product-name') || '').toLowerCase();
            var matchesSearch = name.indexOf(term) > -1;
            var matchesCategory = category === 'all' || card.getAttribute('data-category') === category;
            card.style.display = (matchesSearch && matchesCategory) ? '' : 'none';
        });
    }

    if (searchInput) {
        searchInput.addEventListener('input', applyProductFilters);
    }
    if (categoryChips.length) {
        categoryChips.forEach(function (chip) {
            chip.addEventListener('click', function (e) {
                e.preventDefault();
                categoryChips.forEach(function (c) { c.classList.remove('active'); });
                chip.classList.add('active');
                applyProductFilters();
                history.replaceState(null, '', chip.getAttribute('href'));
            });
        });

        // Honor ?category= on page load (e.g. linked from homepage category tiles)
        var initialParams = new URLSearchParams(window.location.search);
        var initialCategory = initialParams.get('category');
        if (initialCategory) {
            var matchingChip = document.querySelector('.filter-chips a[data-category="' + initialCategory + '"]');
            if (matchingChip) {
                categoryChips.forEach(function (c) { c.classList.remove('active'); });
                matchingChip.classList.add('active');
            }
        }
        applyProductFilters();
    }
});
