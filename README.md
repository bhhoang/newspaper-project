# newspaper-project

## Table of content

![image](https://i.pinimg.com/736x/d3/ce/4e/d3ce4e9df5f6d02e51b4e6f25c021720--icon-design-newspaper.jpg)

<details open="open">
    <summary="Table of Contents"></summary>
        <ol>
            <li><a href="#Introduction">Introduction</a></li>
            <li><a href="#Member List">Group Member</a></li>
        </ol>
</details>

## I - Introduction

1. Newspaper Management System
    - This is the project to implement Newspaper Management System
    - We use mongodb to store a collections of news
2. Workflows
    - Config database host (mongodb) in the base.conf
    - On start app, create cache folder
    - Using requests to download preview image for main page
    - User click on category:
        - Show the list of articles in that category as a scroll list
    - User click on an article:
        - Show the article
        - User click logo or category then switch page
    - User click on login:
        - Login to become an author
        - Save state to cache
        - Author click on Articles
            - Show Articles Management Window
                - Click on Add Article
                    - Show Add Article Window
                        - Fill in the form
                        - Click on Add
                            - Close Add Article Window
                            - Update to the database
                        - Click on Cancel
                            - Close Add Article Window
                - Click on Delete Article
                    - Show Delete Article Window
                        - Choose articles to delêt
                        - Click on Delete
                            - Confirm delete, delted choosen articles
                            - Update to the database
                        - Click on Cancel
                            - Close Delete Article Window
        - Author logout
    - User exit app
    - Delete temporary articles file in cache folder

3. Requirements
    - Python
    - MongoD
    - PyMongo 
    - PyQt6 
## II - Member List
|Name|Student ID|Department|Contribute over 20|
|:-:|:-:|:-:|:-:|
|Bùi Huy Hoàng|BI12-170|ICT|20|
|Nguyễn Duy An|BI12-006|ICT|20|
|Đinh Khánh Minh|BI12-265|CS|12|
|Lê Vũ Hoàng Linh|BI12-243|CS|17|
|Nguyễn Hoàng Dương|BI12-120|DS|17|

## III - Features
- [x] Login
- [x] Logout
- [x] Add article
- [x] Delete article
- [x] Show article
- [x] Show list of articles
- [x] Show list of categories
- [x] Edit profile

## IV - How to run
1. Install python
- For Windows: Download and install python from [here](https://www.python.org/downloads/)
- For Linux: Install python by using command
```bash
sudo apt install python3
```
2. Install pip
- For Windows: Download and install pip from [here](https://pip.pypa.io/en/stable/installing/)
- For Linux: Install pip by using command
```bash
sudo apt install python3-pip
```

3. Install and use virtualenv (optional)
- To install virtualenv, using pip
```bash
pip install virtualenv
```
- Create virtual environment
```bash
virtualenv venv
```
- Activate virtual environment
    - On windows
    ```bash
    venv\Scripts\activate
    ```
    - On Linux/Mac

    ```bash
    source venv/bin/activate
    ```
4. Install dependencies
```bash
pip install -r requirements.txt
```
5. Run app
```bash
python main.py
```
6. Deactivate virtual environment
```bash
deactivate
```

## V - Changelogs

### 04/16/2023 
- Thay đổi base.conf (còn host cho database và icon)
- Fix taskbar hiển thị icon của python thay vì của app
- Thay đổi hàm create_author. Thêm parameter cho email
- Chỉnh sửa hàm hash_password và check_password trong models/methods.py cho chạy chính xác hơn
- Thêm hàm _check_exist_email trong models/dbqueqry.py
- register.ui giờ có thêm trường điền email
- TODO: Xóa pointer-event trong stylesheet của register.ui vì mỗi lần mở đều print ra terminal Unknown property pointer-events    

### 04/17/2023
- Hoàn thành login logic, register logic.
- 1 thay đổi với Data_Articles. Giờ có thêm preview_img
- Thay đổi cách bộ nhớ đệm lưu trữ thông tin
- Giờ mọi thứ liên quan đến current_user sẽ làm việc qua ./cache/json
- Thay đổi cách lưu trữ ảnh trong database

### 04/18/2023
- Hoàn thành chức năng thêm bài viết
- Hoàn thành chức năng xóa bài viết
- Hoàn thành chức năng hiển thị bài viết
- Hoàn thành chức năng hiển thị Profile
- Hoàn thành chức năng Edit Profile
- File new_ui_alpha.py -> main.py
- Decompose main.py

### 04/19/2023
- Xoá icon trong base.conf
- Sửa requirements.txt (bị thiếu pymongo)
- Sửa README.md, thêm changelog