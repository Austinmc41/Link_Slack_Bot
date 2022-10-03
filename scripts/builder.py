def construct_payload(HEADER_BLOCK, DIVIDER_BLOCK, MESSAGE_BLOCK):

    return {
        "channel": "C043C9LA7JT",
        "username": "Link_Bot",
        "icon_emoji": ":robot_face:",
        "text": ":wave: Oh no! Broken links :(",
        "blocks": [
            HEADER_BLOCK,
            DIVIDER_BLOCK,
            MESSAGE_BLOCK
        ],
    }