const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_comment");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

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

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        let commentId = e.target.getAttribute("data-comment-id");
        deleteConfirm.href = `/restaurant/${restaurantSlug}/delete_comment/${commentId}/`;
        deleteModal.show();
    });
}

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