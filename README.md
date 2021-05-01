# [WIP]teleop_pose_vrc
## Video
https://youtu.be/9PCW41RTDNQ

## Description
VRChat上のオブジェクト位置をshaderで画面に出力し、出力映像を読み取ってROSのposeメッセージとして配信します。(現在位置のみの配信)

## Requirements
下記環境で開発、動作確認しています。

* VRChat側PC
  * Windows10
  * Python 3.8
  * OBS Studio
* ロボット側PC
  * Ubuntu18.04
  * ROS Melodic

## Installation
1. [VRChat上のオブジェクト位置表示用のshader](https://github.com/Kuwamai/shader_practice/blob/master/Assets/PoseMarker/PoseMarker.shader)を用いてVRChatワールドを作ります
1. 下記コマンドで使用するライブラリをインストールします
    ```
    $ pip install opencv-python
    $ pip install roslibpy
    $ pip install service_identity
    ```
1. 下記コマンドでリポジトリをcloneします
    ```
    $ git clone https://github.com/Kuwamai/teleop_pose_vrc.git
    ```

## Usage
1. ロボット制御用PCでrosbridge serverを起動します
    ```
    $ roslaunch rosbridge_server rosbridge_websocket.launch
    ```
1. VRChat側PCでVRChatを起動し、OBS StudioでVRChatのゲーム画面を仮想カメラ配信します
1. 下記コマンドのip_addressをROSが起動している端末のipアドレスに置き換え、VRChat側PCで実行します
    ```
    $ python teleop_pose_vrc.py ip_address
    ```

## License
This repository is licensed under the MIT license, see [LICENSE](./LICENSE).
