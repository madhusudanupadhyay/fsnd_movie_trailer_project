$(document).on('click', '.movie-tile', function(event) {
    const ytId = $(this).attr('data-trailer-youtube-id');

    const sourceUrl = 'https://www.youtube.com/embed/' +
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

// Pause the video when the modal is closed
$(document).on('click', '.hanging-close, .modal-backdrop, .modal', function(event) {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $("#trailer-video-container").empty();
    $("#trailer").css("display", "none");
});