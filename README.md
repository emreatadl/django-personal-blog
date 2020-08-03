# AtadilBlog

[![N|Solid](https://intuz-site.imgix.net/uploads/django.png)](https://www.djangoproject.com/download/)

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


# AtadilBlog Kullanılabilir Özellikler

  - Google Analytics
  - Google Tag Manager 
  - CMS
  - Heroku bağlantısı


This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Atadil Blog uses a number of open source projects to work properly:

* [Python] - 
* [Django]
* [HTML5]
* [Javascript]
* [jQuery]


### Installation

Python 3.7 ile yazılmıştır. 
Projeyi indirip aşağıdaki komutlar ile localde siteyi inceleyebilirsiniz.

```sh
$ git clone https://github.com/emreatadl/atadil-personal-blog.git
$ cd atadil-personal-blog
$ python3 manage.py runserver 4044
```

### Plugins

| Plugin | PIP |
| ------ | ------ |
| Material Admin | [pip3 install django-material-admin](https://pypi.org/project/django-material-admin?ref=emre.atadil) |
| CkEditor | [pip3 install django-ckeditor==3.6.2.1](https://pypi.org/project/django-ckeditor/3.6.2.1/?ref=emre.atadil) |

### Google Tag Manager & Google Analytics

``` atadil-personal-blog/static/js/analytics.js``` dosyasında bulunan GTM kodunuzu 
> https://github.com/emreatadl/atadil-personal-blog/blob/428ad5c9aada9248fa32fb52b2d3e6636a275fc9/static/js/analytics.js#L4

#### Cloudinary Config
Projede kullandığım cloud için [Cloudinary](https://cloudinary.com/pricing-2020?ref=emre.atadil) ziyaret edip hesap oluşturabilirsiniz.

Cloud bilgilerinizi bu alana girmelisiniz:
```sh
cloudinary.config(
    cloud_name="cloud_name",
    api_key="api_key",
    api_secret="api_secret"
)
```

### CkEditor Kurulumu
```sh
$ pip3 install django-ckeditor==3.6.2.1
```
```json
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}
```


### Todos

 - Add Night Mode

License
----
[MIT](https://github.com/emreatadl/atadil-personal-blog/blob/master/LICENSE.txt)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/emreatadl/atadil-personal-blog/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/emreatadl/atadil-personal-blog/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/emreatadl/atadil-personal-blog/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/emreatadl/atadil-personal-blog/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/emreatadl/atadil-personal-blog/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/emre-atadil/
[product-screenshot]: images/screenshot.png
