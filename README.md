# Rouigram python packaging

Rouigram is a simple and use-full platform for Instagram user id 
without any registration. instagram user_id is the important factor 
to use other API of Instagram for making interconnected application.
[You can help develop this code in the github][src]. 
# How to install 
type in your terminal 
```python
pip install rouigram
```
# Your sample Code
```python
import rouigram as instagram

info = instagram.getInformation("mohammadali_mirhamed")  #define Username

print(instagram.getInformation.user_id(info))  # You will get user id
print(instagram.getInformation.username(info)) # You will get username
print(instagram.getInformation.fullname(info)) # You will get fullname
print(instagram.getInformation.follower_count(info))  # You will get follower count
print(instagram.getInformation.following_count(info)) # You will get following count
print(instagram.getInformation.media_count(info))     # You will get media_count
print(instagram.getInformation.external_url(info))    # You will get Website link
print(instagram.getInformation.is_private(info))      # You will get is_private
print(instagram.getInformation.profile_hd_photo(info))  # You will get FullHd profile Image
print(instagram.getInformation.biography(info))         # You will get biography
```


[Rouigram offcial website : rouigram.pythony.ir ][web].
----
[developet by Mohammadali Mirhamed Roui][rst].

[src]: https://github.com/MohammadaliMirhamed/rouigram.py
[web]: https://www.mirhamedrooy.ir/rouigram/
[rst]: https://www.mirhamedrooy.ir
