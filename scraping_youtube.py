import pandas as pd
import requests
import config


# 親コメントを取得


def get_comment(no, video_id, next_page_token, text_data):
    parameter = {
      'key': config.API_KEY,
      'videoId': video_id,
      'part': 'snippet',
      'order': 'time',
      'textFormat': 'plaintext',
      'maxResults': 100,
    }
    if next_page_token is not None:
        parameter['pageToken'] = next_page_token
    response = requests.get(config.URL + 'commentThreads', params=parameter)
    resource = response.json()
    for comment_data in resource['items']:
        # コメントIDを取得
        parent_id = comment_data['snippet']['topLevelComment']['id']
        # コメントを取得
        text = comment_data['snippet']['topLevelComment']['snippet']['textDisplay']
        # コメントの高評価数を取得
        like_count = comment_data['snippet']['topLevelComment']['snippet']['likeCount']
        # 返信数を取得
        reply_count = comment_data['snippet']['totalReplyCount']
        # コメントしたユーザー名を取得
        user_name = comment_data['snippet']['topLevelComment']['snippet']['authorDisplayName']
        # コメントしたユーザーのチャンネルURL取得
        author_channel = comment_data['snippet']['topLevelComment']['snippet']['authorChannelUrl']
        # 取得した情報をリストに追加
        text_data.append([parent_id, 'parent', text, like_count, reply_count,
                         user_name, author_channel])
        if reply_count > 0:
            cno = 1
            get_reply(no, cno, video_id, next_page_token, parent_id, text_data)
        no = no + 1
    if 'nextPageToken' in resource:
        get_comment(no, video_id, resource['nextPageToken'], text_data)


# 子コメントを取得


def get_reply(no, cno, video_id, next_page_token, comment_post_id, text_data):
    parameter = {
      'key': config.API_KEY,
      'videoId': video_id,
      'part': 'snippet',
      'textFormat': 'plaintext',
      'maxResults': 50,
      'parentId': comment_post_id,
      }
    if next_page_token is not None:
        parameter['pageToken'] = next_page_token
    response = requests.get(config.URL + 'comments', params=parameter)
    resource = response.json()
    for comment_data in resource['items']:
        # コメントを取得
        text = comment_data['snippet']['textDisplay']
        # コメントの高評価数を取得
        like_count = comment_data['snippet']['likeCount']
        # コメントしたユーザー名を取得
        user_name = comment_data['snippet']['authorDisplayName']
        # コメントしたユーザーのチャンネルURLを取得
        author_channel = comment_data['snippet']['authorChannelUrl']
        # 取得した情報をリストに追加
        text_data.append([comment_post_id, 'child', text, like_count, 0,
                          user_name, author_channel])
        cno = cno + 1
    if 'nextPageToken' in resource:
        get_reply(no, cno, video_id, resource['nextPageToken'],
                  comment_post_id, text_data)


# コメントを全て取得し、csvに出力


if __name__ == "__main__":
    id_df = pd.read_csv(config.INPUT_FILE)
    video_id_list = id_df.video_id.to_list()
    brand_list = id_df.brand.to_list()
    columns_list = ['comment_id', 'type', 'comment_data', 'like_count',
                    'reply_count', 'user_name', 'profile_page']
    no = 1
    for (video_id, brand_name) in zip(video_id_list, brand_list):
        text_data = []
        get_comment(no, video_id, None, text_data)
        # 取得したコメントを高評価順にソート
        df = pd.DataFrame(text_data, columns=columns_list)\
            .sort_values('like_count', ascending=False)
        # csvで出力
        df.to_csv(str(config.OUTPUT_PATH) + "/" + brand_name + '.csv',
                  index=False, encoding=config.ENCODING)
