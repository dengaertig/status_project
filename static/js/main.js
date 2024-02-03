
$(document).ready(function () {
    setInterval(function () {
        $('tbody tr').each(function () {
            var url = $(this).find('td:eq(1)').text();
            var row = $(this);
            $.ajax({
                type: 'GET',
                url: '/check_status/?url=' + encodeURIComponent(url),
                success: function (data) {
                    row.find('td:eq(2)').text(data.status);
                    if(data.status == 'Offline'){
                        row.addClass('table-danger');
                    } else{
                        row.addClass('table-success');
                    }
                }     
            });
        });
    }, 3000);
});

