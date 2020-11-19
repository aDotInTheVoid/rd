content = [
    {
        "header": "The Standard Library",
        "content": "Rust's standard library has extensive API documentation, with explanations of how to use various things, as well as example code for accomplishing various tasks.",
        "link": "https://doc.rust-lang.org/stable/std/",
    },
    {
        "header": "The Book",
        "content": """Affectionately nicknamed "the book," The Rust Programming Language will give you an overview of the language from first principles. You'll build a few projects along the way, and by the end, you'll have a solid grasp of the language."""
    }
]


with open("./index.html", "r") as f:
    tpl = f.read()

[head, p1, p2, p3, foot] = tpl.split("<!-- TEMPL -->")

print(head)

for idx, c in enumerate(content):
    if idx == 0:
        t = p1
    elif idx == 1:
        t = p2
    else:
        t = p3
    for i in c:
        t = t.replace(f"<!-- SLOT {i} -->", c[i])

    print(t)

print(foot)