const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_comment");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

document.querySelectorAll('.btn-edit').forEach(button => {
    button.addEventListener('click', function() {
        const commentTextValue = this.getAttribute('data-comment-text');
        const commentId = this.getAttribute('data-comment-id');
        const commentRating = this.getAttribute('data-comment-rating');
        const commentTextarea = document.getElementById('id_comment');
        const ratingSelect = document.getElementById('id_rating');
        const submitButton = document.getElementById('submitButton');
        
        commentTextarea.value = commentTextValue;
        ratingSelect.value = commentRating;
        submitButton.innerText = "Update";
        commentForm.action = `/restaurant/${restaurantSlug}/edit_comment/${commentId}/`;
        document.getElementById('comment-form-card').scrollIntoView({ behavior: 'smooth' });
    });
});

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `/restaurant/${restaurantSlug}/delete_comment/${commentId}/`;
        deleteModal.show();
    });
}