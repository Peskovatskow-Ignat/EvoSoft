import requests
from config import cookies_link, headers_link


def get_user_link(data: dict, list_link: list) -> list[str]:
    """
    Args:
        data (dict): _description_
        list_link (list): _description_

    Returns:
        list[str]: _description_
    """
    if len(list_link) >= 3:
        return
    if isinstance(data, dict):
        if "screen_name" in data and data["screen_name"] != "elonmusk":
            list_link.append("https://twitter.com/" + data.get("screen_name"))

        for key, val in data.items():
            get_user_link(val, list_link)
    elif isinstance(data, list):
        for item in data:
            get_user_link(item, list_link)


def get_post(posts_id: str) -> dict[any, any]:
    from config import proxies
    """
    Args:
        posts_id (str): _description_

    Returns:
        dict[any, any]: _description_
    """
    proxies = proxies

    cookies = cookies_link
    
    headers_link['referer'] = headers_link['referer'].format(posts_id = posts_id)
    
    
    params = {
        "variables": '{"focalTweetId":"'
        + posts_id
        + '","with_rux_injections":false,"includePromotedContent":true,"withCommunity":true,"withQuickPromoteEligibilityTweetFields":true,"withBirdwatchNotes":true,"withVoice":true,"withV2Timeline":true}',
        "features": '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
        "fieldToggles": '{"withArticleRichContentState":true}',
    }

    posted_info = requests.get(
        "https://twitter.com/i/api/graphql/ZkD-1KkxjcrLKp60DPY_dQ/TweetDetail",
        headers=headers_link,
        params=params,
        cookies=cookies,
        proxies=proxies,
    ).json()

    list_link = []

    get_user_link(posted_info, list_link)

    return list_link
