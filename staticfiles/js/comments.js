const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_comment");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const ratingInput = document.getElementById("id_rating");

document.getElementById('write-comment-icon').addEventListener('click', function() {
    if (userIsAuthenticated === "false") {
        var loginModal = new bootstrap.Modal(document.getElementById('loginModal'));
        loginModal.show();
    } else {
        document.getElementById('comment-form-card').scrollIntoView({ behavior: 'smooth' });
    }
});

document.querySelectorAll('.btn-edit').forEach(button => {
    button.addEventListener('click', function() {
        const commentTextValue = this.getAttribute('data-comment-text');
        const commentId = this.getAttribute('data-comment-id');
        const commentTextarea = document.getElementById('id_comment');
        const submitButton = document.getElementById('submitButton');
        commentTextarea.value = commentTextValue;
        submitButton.innerText = "Update";
        commentForm.action = `/restaurant/${restaurantSlug}/edit_comment/${commentId}/`;
        document.getElementById('comment-form-card').scrollIntoView({ behavior: 'smooth' });
    });
});

document.querySelectorAll('.rating-input .fa-star').forEach(star => {
    star.addEventListener('click', function() {
        const ratingValue = this.getAttribute('data-value');
        ratingInput.value = ratingValue;
        updateStars(ratingValue);
    });
});

function updateStars(rating) {
    document.querySelectorAll('.rating-input .fa-star').forEach(star => {
        if (parseInt(star.getAttribute('data-value')) <= rating) {
            star.classList.remove('far');
            star.classList.add('fas');
        } else {
            star.classList.remove('fas');
            star.classList.add('far');
        }
    });
}