import requests
from random import randint
from time import sleep
from get_link_func import get_post
from config import cookies_post, proxies


def get_post_text(data, new_list: list) -> None:
    """Извлекает текст постов из вложенных словарей.

    Args:
        data: Данные для извлечения текста постов.
        new_list (list): Список, в который будут добавляться извлеченные тексты постов.

    Returns:
        None
    """
    if len(new_list) >= 10:
        return
    if isinstance(data, dict):
        if "full_text" in data and "quoted_status_permalink" in data:
            new_list.append(
                {
                    "id": len(new_list) + 1,
                    "text": data["full_text"],
                    "id_post": data["id_str"],
                }
            )

        for key, val in data.items():
            if "quoted_status_result" not in key:
                if "tweets" not in key:
                    get_post_text(val, new_list)
    elif isinstance(data, list):
        for item in data:
            get_post_text(item, new_list)


cookies = cookies_post

headers = {
    "authority": "twitter.com",
    "accept": "*/*",
    "accept-language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
    "content-type": "application/json",
    # 'cookie': 'd_prefs=MToxLGNvbnNlbnRfdmVyc2lvbjoyLHRleHRfdmVyc2lvbjoxMDAw; guest_id_ads=v1%3A170257767914293732; guest_id_marketing=v1%3A170257767914293732; _ga=GA1.2.254564089.1707482684; kdt=5e2DwdFToW6hlqasqoko2ku8DFoRJBpiIiNVimix; dnt=1; twtr_pixel_opt_in=Y; personalization_id="v1_gSVcSaKJR6A4hat1JrmlfA=="; guest_id=v1%3A170751575112713138; auth_token=887a924e109694f2db77c20f23f99538e1501d2f; ct0=e4156d684f6c6cb84524c937e5139c4577fbae366a10e1dc180ffba07a8e4159de7f31a85f807e6b343ab98951881337d760752ff305b1ce5227228a0448609989f7af8c3f1eef968a530efc81efc641; twid=u%3D1755981700645924864; lang=en; _gid=GA1.2.588222515.1710254555; external_referer=padhuUp37zhU%2Fo1ilYwCNOmtabS4UqDS|0|8e8t2xd8A2w%3D',
    "referer": "https://twitter.com/elonmusk",
    "sec-ch-ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0",
    "x-client-transaction-id": "J/96Sk5rGCFCMna04IVzge0f4AJJeSiUMcKFarxbG1Yiye5O8qd4rqBUd2bW3mPpubl8hiZRgY1us/BFH2p3CvejlW+dJg",
    "x-csrf-token": "e4156d684f6c6cb84524c937e5139c4577fbae366a10e1dc180ffba07a8e4159de7f31a85f807e6b343ab98951881337d760752ff305b1ce5227228a0448609989f7af8c3f1eef968a530efc81efc641",
    "x-twitter-active-user": "yes",
    "x-twitter-auth-type": "OAuth2Session",
    "x-twitter-client-language": "en",
}

params = {
    "variables": '{"userId":"44196397","count":20,"includePromotedContent":true,"withQuickPromoteEligibilityTweetFields":true,"withVoice":true,"withV2Timeline":true}',
    "features": '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
}

response = requests.get(
    "https://twitter.com/i/api/graphql/WwS-a6hAhqAAe-gItelmHA/UserTweets",
    params=params,
    cookies=cookies,
    headers=headers,
    proxies=proxies,
).json()


if __name__ == "__main__":

    posted_list = []
    get_post_text(response, posted_list)

    sleep(randint(3, 7))
    for value in posted_list:
        list_link = get_post(value.get("id_post"))
        sleep(randint(5, 10))
        print(f"Post id: {value.get('id')}")
        print(f"    text: {value.get('text')}")
        print(f"        link_user: {', '.join(list_link)}")
