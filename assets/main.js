$(document).on('click', '.movie-tile', function(event) {
    const ytId = $(this).attr('data-trailer-youtube-id');

    const sourceUrl = 'http://www.youtube.com/embed/' +
        ytId +
        '?autoplay=1&html5=1';

    $("#trailer").css("display", "flex");

    $("#trailer-video-container").empty().append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
    }));
});