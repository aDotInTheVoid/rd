# TODO: Pritty SVG's
# TODO: Some sort of order
# SVG's should be likg
# <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" class="h-8 w-8 md:h-10 md:w-10 md:-my-1">
#   <g>
#     <path class="fill-current text-gray-400" d="M12 21a2 2 0 0 1-1.41-.59l-.83-.82A2 2 0 0 0 8.34 19H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h4a5 5 0 0 1 4 2v16z" />
#     <path class="fill-current text-gray-700" d="M12 21V5a5 5 0 0 1 4-2h4a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1h-4.34a2 2 0 0 0-1.42.59l-.83.82A2 2 0 0 1 12 21z" />
#   </g>
# </svg>


def make_img(link):
    return f"""<img class="h-32 w-32 md:h-22 md:w-22 md:-my-1" src="{link}"/>"""


content = [
    {
        "header": "Rust Analyzer",
        "content": "Bringing a great IDE experience to the Rust programming language.",
        "link": "https://rust-analyzer.github.io/manual.html",
        "linkname": "Read the Rust Analyzer manual",
        "img": "./ra.svg",
    },
    {
        "header": "Learn Rust With Entirely Too Many Linked Lists",
        "content": "While linked lists arn't a great data strutcture, implemeenting them can teach us a lot about rust",
        "link": "https://rust-unofficial.github.io/too-many-lists/",
        "linkname": "Write a bajillion linked lists.",
        "img": "./link.svg"
    },
    {
        "header": "Proc macro workshop",
        "content": "Contains a selection of projects designed to learn to write Rust procedural macros — Rust code that generates Rust code.",
        "link": "https://github.com/dtolnay/proc-macro-workshop",
        "linkname": "Learn about proc macros",
    },
    {
        "header": "The Little Book of Rust Macros",
        "content": "Documentation on writing macros by example",
        "link": "https://danielkeep.github.io/tlborm/book/index.html",
        "linkname": "Read about macros",
    },
    {
        "header": "Writing an OS in Rust",
        "content": "This blog series creates a small operating system in rust.",
        "link": "https://os.phil-opp.com/",
        "linkname": "Read the os blog",
    },
    {
        "header": "The Rust Performance Book.",
        "content": "This book contains many techniques that can improve the performance—speed and memory usage—of Rust programs.",
        "link": "https://nnethercote.github.io/perf-book/introduction.html",
        "linkname": "Read the performance book",
        "img": "./speedometer.svg",
    },
    {
        "header": "The async book",
        "content": "Documentation on learning asyncronus rust, which allows other parts of the progamm to keep running while one is blocked on something like IO.",
        "link": "https://rust-lang.github.io/async-book/",
        "linkname": "Read the async book",
    },
    {
        "header": "Embedded Rust documentation",
        "content": "All the documentation provided by the Rust and WebAssembly Working Group.",
        "link": "https://docs.rust-embedded.org/",
        "linkname": "Learn about embedded rust",
        "img": "./embedded.svg"
    },
    {
        "header": "Rust Webassembly documentations",
        "content": "All the documentation provided by the WebAssembly Working Group.",
        "link": "https://rustwasm.github.io/docs.html",
        "linkname": "Learn about rust and webassembly",
        "img": "./wasm-ferris.png"
    },
    {
        "header": "The rust cli book",
        "content": "Describes the rust ecosystem for creating command line apps",
        "link": "https://rust-cli.github.io/book/index.html",
        "linkname": "Read the cli book",
    },
    {
        "header": "FFI Omnibus",
        "content": "A collection of examples of using code written in Rust from other languages.",
        "link": "http://jakegoulding.com/rust-ffi-omnibus/",
        "linkname": "Read the ffi omnibus",
    },
    {
        "header": "bindgen",
        "content": "bindgen automatically generates Rust FFI bindings to C and C++ libraries.",
        "link": "https://rust-lang.github.io/rust-bindgen/",
        "linkname": "Read the bindgen docs",
    },
    {
        "header": "mdBook",
        "content": "mdBook is a command line tool to create books using Markdown files. Most of these books were made with it.",
        "link": "https://rust-lang.github.io/mdBook/",
        "linkname": "Read the mdBook documentation",
    },
    {
        "header": "The Rust Forge",
        "content": "The Rust Forge serves as a repository of miscelanius supplementary documentation useful for Rust contributors",
        "link": "https://forge.rust-lang.org/",
        "linkname": "Visit the forge",
    },
    {
        "header": "Clippy documentation",
        "content": "A bunch of lints to catch common mistakes and improve your Rust code.",
        "link": "https://rust-lang.github.io/rust-clippy/stable/",
        "linkname": "See the clippy links",
    },
    {
        "header": "This week in rust",
        "content": "Stay up to date with events, learning resources, and recent developments in Rust community.",
        "link": "https://this-week-in-rust.org/",
        "linkname": "See whats new this week",
    },
    {
        "header": "timetill.rs",
        "content": " A website for upcoming Rust conferences.",
        "link": "https://timetill.rs/",
        "linkname": "See upcoming events",
    },
    {
        "header": "Rustup components availability",
        "content": "Monitors rustup components availability history on different platforms.",
        "link": "https://rust-lang.github.io/rustup-components-history/",
        "linkname": "See the component history",
    },
    {
        "header": "The Rust Fuzzing Book",
        "content": "Describes how to fuzz code written in rust",
        "link": "https://rust-fuzz.github.io/book/",
        "linkname": "Read the fuzzing book",
    },
    {
        "header": "Rust by Example",
        "content": "Rust by Example is a collection of runnable examples that illustrate various Rust concepts and standard libraries.",
        "link": "https://doc.rust-lang.org/rust-by-example/",
        "linkname": "Check out Rust by Example",
    },
    {
        "header": "lib.rs",
        "content": "Fast, lightweight, opinionated, unofficial alternative to crates.io.",
        "link": "https://lib.rs/",
        "linkname": "Check out lib.rs",
    },
    {
        "header": "docs.rs",
        "content": "Docs.rs hosts documentation for all the crates on crates.io.",
        "link": "https://docs.rs/",
        "linkname": "Check out crate docs",
    },
    {
        "header": "crates.io",
        "content": "crates.io is the Rust community's central package registry that serves as a location to discover and download packages.",
        "link": "https://crates.io/",
        "linkname": "Check out crates.io",
    },
    {
        "header": "Chalk",
        "content": "Chalk is a library that implements the Rust trait system. The implementation is meant to be practical and usable, but also high-level enough to map easily to a full specification. It is also meant to be an independent library that can be integrated both into the main rustc compiler and also other programs and contexts.",
        "link": "https://rust-lang.github.io/chalk/book/",
        "linkname": "Read the chalk docs",
    },
    {
        "header": "Rustup documentation",
        "content": "rustup installs The Rust Programming Language from the official release channels, enabling you to easily switch between stable, beta, and nightly compilers and keep them updated.",
        "link": "https://rust-lang.github.io/rustup/",
        "linkname": "Read the rustup docs",
    },
    {
        "header": "Rustc dev guide",
        "content": "This guide is meant to help document how rustc – the Rust compiler – works, as well as to help new contributors get involved in rustc development.",
        "link": "https://rustc-dev-guide.rust-lang.org/",
        "linkname": "Read the dev guide",
    },
    {
        "header": "The Reference",
        "content": "It describes each language construct and their use, memory model, concurrency model, runtime services, linkage model, and debugging facilities",
        "link": "https://doc.rust-lang.org/reference/",
        "linkname": "Read the reference",
        "img": "./reference.svg"
    },
    {
        "header": "The Rustonomicon",
        "content": """THE KNOWLEDGE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF UNLEASHING INDESCRIBABLE HORRORS THAT SHATTER YOUR PSYCHE AND SET YOUR MIND ADRIFT IN THE UNKNOWABLY INFINITE COSMOS.""",
        "link": "https://doc.rust-lang.org/nomicon/",
        "linkname": "Dig into all the awful details",
        "img": "./nomicon.svg"
    },
    {
        "header": "Edition Guide",
        "content": """"Editions" are Rust's way of communicating large changes in the way that it feels to write Rust code. This guide contains the content of editions, as well as migration instructions""",
        "link": "https://doc.rust-lang.org/stable/edition-guide/",
        "linkname": "Read the edition guide",
    },
    {
        "header": "Unsafe Code Guidelines",
        "content": """This document is produced by the UCG WG to provide a "guide" for writing unsafe code that "recommends" what kinds of things unsafe code can and cannot do, and that documents which guarantees unsafe code may rely on. It is largely a work-in-progress right now.""",
        "link": "https://rust-lang.github.io/unsafe-code-guidelines",
        "linkname": "Read the guidelines",
    },
    {
        "header": "Active RFCs",
        "content": "These are nominations to stabilize something",
        "link": "https://rfcbot.rs/",
        "linkname": "See active RFCs",
    },
    {
        "header": "Adopted RFCs",
        "content": "These are the RFCs that have been approved",
        "link": "https://rust-lang.github.io/rfcs/",
        "linkname": "Read the RFCs",
    },
    {
        "header": "thanks.rust-lang.org",
        "content": "Thanks is a place for us to give thanks to everyone who contributes to the Rust project.",
        "link": "https://thanks.rust-lang.org/",
        "linkname": "Be thankfull",
    },
    {
        "header": "Rust API Guidelines",
        "content": "This is a set of recommendations on how to design and present APIs for the Rust programming language. They are authored largely by the Rust library team, based on experiences building the Rust standard library and other crates in the Rust ecosystem.",
        "link": "https://rust-lang.github.io/api-guidelines/",
        "linkname": "Read the api guidelines",
    },
    {
        "header": "Rust Blog",
        "content": "This blog is used for anouncements that effect all rust users, like releases and important projects",
        "link": "https://blog.rust-lang.org/",
        "linkname": "Read the rust blog",
    },
    {
        "header": "Inside Rust Blog",
        "content": "This blog is aimed at those who wish to follow along with Rust development. The various Rust teams and working groups use this blog to post status updates, calls for help, and other similar announcements.",
        "link": "https://blog.rust-lang.org/inside-rust/",
        "linkname": "Read the inside rust blog",
    },
    {
        "header": "The Rustc Book",
        "content": "Rustc is the rust compiller. Most Rust programmers don't invoke rustc directly, but instead do it through Cargo. But it can still be good to know how it works",
        "link": "https://doc.rust-lang.org/rustc/",
        "linkname": "Read the rustc book",
    },
    {
        "header": "The Cargo Book",
        "content": "Cargo is the Rust package manager. It Cargo downloads your Rust package’s dependencies, compiles your packages, makes distributable packages, and uploads them to crates.io",
        "link": "https://doc.rust-lang.org/cargo/",
        "linkname": "Read the cargo book",
    },
    {
        "header": "Unstable book",
        "content": "This book has documentation of the nighly features that haven't been stabilized yet",
        "link": "https://doc.rust-lang.org/unstable-book/",
        "linkname": "Read the Unstable book",
        "img": "./unstable.svg"
    },
    {
        "header": "Rustfmt",
        "content": "Rustfmt is the code formatter for rust",
        "link": " https://rust-lang.github.io/rustfmt/?version=master&search=",
        "linkname": "Rustfmt configuration",
    },
    {
        "header": "The Standard Library",
        "content": "Rust's standard library has extensive API documentation, with explanations of how to use various things, as well as example code for accomplishing various tasks.",
        "link": "https://doc.rust-lang.org/stable/std/",
        "linkname": "Check out the standard library",
    },
    {
        "header": "The Book",
        "content": """Affectionately nicknamed "the book," The Rust Programming Language will give you an overview of the language from first principles. You'll build a few projects along the way, and by the end, you'll have a solid grasp of the language.""",
        "linkname": "Read the book",
        "link": "https://doc.rust-lang.org/stable/book/index.html",
    },
    {
        "header": "Error listing",
        "content": "Many of Rust's errors come with error codes, and you can request extended diagnostics from the compiler on those errors. You can also read them online, if you prefer to read them that way.",
        "link": "https://doc.rust-lang.org/stable/error-index.html",
        "linkname": "See the errors",
    },
    {
        "header": "Bors Queue",
        "content": "Bors is rust's CI bot, that keeps master green. The queue has all the PRs that have been approved and are waiting to be merged",
        "link": "https://bors.rust-lang.org/queue/all",
        "linkname": "See whats coming",
    },
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
    img = c.get("img")
    if img is not None:
        t = t.replace(f"<!-- SLOT svg -->", make_img(img))

    print(t)

print(foot)
