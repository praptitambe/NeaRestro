const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_comment");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

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
        console.log(commentId);
        deleteConfirm.href = `/restaurant/${restaurantSlug}/delete_comment/${commentId}/`;
        deleteModal.show();
    });
}