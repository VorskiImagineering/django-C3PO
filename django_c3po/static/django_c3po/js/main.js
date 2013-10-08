$(function() {
    var taskUrl = $('#task-url');

    var checkState = function() {
        if (taskUrl.val()) {
            $.ajax({
                url: taskUrl.val(),
                type: 'get',
                success: function(result) {
                    if (result) {
                        $('#info').text('Translations synchronized.');
                        $('#task-url').val('');
                    } else {
                        $('#info').append('.');
                    }
                }
            });
            setTimeout(checkState, 3000);
        }
    }
    setTimeout(checkState, 3000);
});
