## Youtuber & Vtuber API
Youtuber, Vtuberの情報を返すAPIです

随時更新中! 誰でも追加、更新できます

```
curl -s 'https://youtuberapi.herokuapp.com/api/?format=json' | jq .
{
  "vtuber": "https://youtuberapi.herokuapp.com/api/vtuber/?format=json",
  "youtuber": "https://youtuberapi.herokuapp.com/api/youtuber/?format=json"
}
```
Vtuberの情報が欲しい場合は、
https://youtuberapi.herokuapp.com/api/vtuber/?format=json

Youtuberの情報が欲しい場合は,
https://youtuberapi.herokuapp.com/api/youtuber/?format=json


  ### Response

|パラメータ名     |値 |有無|説明|例|
| :------------|:-----|:-------|:----------|:-----|
| id           |Number|◯|ユニークなID|2|
| name         |String|◯|名前|"輝夜月"|
| nickname     |String|-|ニックネーム、別名|"none"|
| belong       |String|-|所属事務所、チーム|"THE MOON STUDIO"|
| twiiter      |String|-|Twiiter ID|"KaguyaLuna"|
| channel_id   |String|◯|Youtubeのchannel ID|"UCMYtONm441rBogWK_xPH9HA"|
| tag          |String|-|偏見でタグ付したもの|"可愛い"|

※有無の欄に○が無い物は"none"が返ってきます。
※※belongのところは所属がなかったら"無所属"が返ってくる

レスポンス例
```
curl -s 'https://youtuberapi.herokuapp.com/api/vtuber/?format=json' | jq .
[
  {
    "id": 1,
    "name": "キズナアイ",
    "nickname": "親分",
    "belong": "upd8",
    "twiiter": "aichan_nel",
    "channel_id": "UC4YaOt1yT-ZeyB0OmxHgolA",
    "tag": "可愛い"
  },
  {
    "id": 2,
    "name": "輝夜月",
    "nickname": "none",
    "belong": "THE MOON STUDIO",
    "twiiter": "KaguyaLuna",
    "channel_id": "UCQYADFw7xEJ9oZSM5ZbqyBw",
    "tag": "可愛い"
  },
  {
    "id": 3,
    "name": "ミライアカリ",
    "nickname": "none",
    "belong": "Mirai Akari Project",
    "twiiter": "MiraiAkari_prj",
    "channel_id": "UCMYtONm441rBogWK_xPH9HA",
    "tag": "記憶喪失"
  },
  ```

### Request
|リクエストパラメータ名|値 |説明|例|
| :----------------|:-----|:----------|:-----|
| name               |String|名前|"赤毛のとも"|
| belong             |String|所属|"無所属"|
| tag                |String|tag検索用|"ゲーム実況"|

リクエスト例
```
curl -s 'https://youtuberapi.herokuapp.com/api/youtuber/?format=json&belong=無所属&tag=ゲーム実況' | jq .
[
  {
    "id": 1,
    "name": "赤髪のとも",
    "nickname": "none",
    "belong": "無所属",
    "twiiter": "tomo0723sw",
    "channel_id": "UCEIMvzf3R9d3_2A3IAajvHg",
    "tag": "ゲーム実況"
  },
  {
    "id": 2,
    "name": "あいたかはしくん",
    "nickname": "none",
    "belong": "無所属",
    "twiiter": "itakahashikun",
    "channel_id": "UCT7tMScWlVnzbbREcSQVPmg",
    "tag": "ゲーム実況"
  },
  {
    "id": 3,
    "name": "弟者",
    "nickname": "none",
    "belong": "無所属",
    "twiiter": "Otojya",
    "channel_id": "UC2GuoutVyegg6PUK88lLpjw",
    "tag": "ゲーム実況"
  }
]
```

情報ソースとして

[vtuber post](https://vtuber-post.com)

[Youtuber大図鑑](http://youtuberber.net)
