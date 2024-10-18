from fastapi import FastAPI

from App import App

app = FastAPI()


def create_app_list() -> list[App]:
    app1 = App(
        img_resource="https://play-lh.googleusercontent.com"
                     "/n8phgc3uELWG1TgNiZ5F70UAwW_GHyFusTGvZJEvmf36bO9qsRJ5dgXZSOWfuHGs3dM=w480-h960",
        description="PDF Scanner and document organizer.",
        name="HandyDocs - Document organizer",
        playstore_link="https://play.google.com/store/apps/details?id=com.alphaomardiallo.handydocs"
    )

    app2 = App(
        img_resource="https://play-lh.googleusercontent.com/VherVAP2-12WTetnu4XHUlBaG7RtIzynd9bdWrqorJ2LFDHgw"
                     "-bkoh9AICNPiUtjcA=w480-h960",
        description="Check if your email has been in a data breach",
        name="Pwned App",
        playstore_link="https://play.google.com/store/apps/details?id=com.alphaomardiallo.pawnedemail"
    )
    return [app1, app2]


@app.get("/")
def read_root():
    return {"apps": create_app_list()}
