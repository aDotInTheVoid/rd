# TODO: Pritty SVG's

# https://rust-unofficial.github.io/too-many-lists/
# https://danielkeep.github.io/tlborm/book/index.html
# https://os.phil-opp.com/
# https://nnethercote.github.io/perf-book/introduction.html
# https://rust-lang.github.io/async-book/
# https://github.com/rust-lang/rust/tree/master/src/doc
# https://docs.rust-embedded.org/
# https://rustwasm.github.io/docs.html
# https://rust-cli.github.io/book/index.html
# https://doc.rust-lang.org/stable/
# http://jakegoulding.com/rust-ffi-omnibus/
# https://rust-lang.github.io/rust-bindgen/
# https://rust-lang.github.io/mdBook/
# https://forge.rust-lang.org/
# https://rust-lang.github.io/rust-clippy/
# https://this-week-in-rust.org/
# https://timetill.rs/#/
# https://rust-lang.github.io/rustup-components-history/
# https://rust-fuzz.github.io/book/introduction.html
# https://doc.rust-lang.org/rust-by-example/index.html
# https://lib.rs/
# https://docs.rs/
# https://crates.io/
# https://rust-lang.github.io/chalk/book/
# https://rust-lang.github.io/rustup/
# https://rustc-dev-guide.rust-lang.org/
# https://doc.rust-lang.org/nightly/reference/
# https://doc.rust-lang.org/nomicon/
# https://doc.rust-lang.org/stable/edition-guide/
# https://rust-lang.github.io/unsafe-code-guidelines
# https://rfcbot.rs/
# https://rust-lang.github.io/rfcs/
# https://thanks.rust-lang.org/
# https://rust-lang.github.io/api-guidelines/
# https://blog.rust-lang.org/
# https://blog.rust-lang.org/inside-rust/index.html
# https://doc.rust-lang.org/rustc/
# https://doc.rust-lang.org/cargo/
# https://doc.rust-lang.org/unstable-book/
# https://rust-lang.github.io/rustfmt/?version=master&search=

content = [
    {
        "header": "The Standard Library",
        "content": "Rust's standard library has extensive API documentation, with explanations of how to use various things, as well as example code for accomplishing various tasks.",
        "link": "https://doc.rust-lang.org/stable/std/",
        "linkname": "Check out the standard library"
    },
    {
        "header": "The Book",
        "content": """Affectionately nicknamed "the book," The Rust Programming Language will give you an overview of the language from first principles. You'll build a few projects along the way, and by the end, you'll have a solid grasp of the language.""",
        "linkname": "Read the book",
        "link": "https://doc.rust-lang.org/stable/book/index.html"
    },
    {
        "header": "Error listing", 
        "content": "Many of Rust's errors come with error codes, and you can request extended diagnostics from the compiler on those errors. You can also read them online, if you prefer to read them that way.",
        "link": "https://doc.rust-lang.org/stable/error-index.html",
        "linkname": "See the errors"
    },
    {
        "header": "Bors Queue",
        "content": "Bors is rust's CI bot, that keeps master green. The queue has all the PRs that have been approved and are waiting to be merged",
        "link": "https://bors.rust-lang.org/queue/all",
        "linkname": "See whats coming"
    }
]


with open("./index.html", "r") as f:
    tpl = f.read()

# The first 2 cards have different css, so we do this
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