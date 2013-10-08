$(function() {
    var taskUrl = $('#task-url');

    var checkState = function() {
        if (taskUrl.val()) {
            $.ajax({
                url: taskUrl.val(),
                type: 'get',
                success: function(data) {
                    if (data['ready']) {
                        if (data['error']) {
                            $('#error').addClass('visible')
                                    .html(data['error'].replace(/\n/g, '<br />'));
                        } else {
                            $('#error').removeClass('visible');
                        }

                        if (data['info']) {
                            $('#info').addClass('visible')
                                    .html(data['info'].replace(/\n/g, '<br />'));
                        } else {
                            $('#info').removeClass('visible');
                        }
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
