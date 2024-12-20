class App:
    def __init__(self, img_resource: str, description: str, name: str, playstore_link: str):
        self.img_resource = img_resource
        self.description = description
        self.name = name
        self.playstore_link = playstore_link


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

    app3 = App(
        img_resource="https://play-lh.googleusercontent.com"
                     "/AK1JvTkQZo9QNfMZzBdn8n7H_qTfzogIrtougHvppqnucuneIAF2J0OLcEn8ES29x34=w480-h960",
        description="Track and share your 100 days of code challenge",
        name="100DOC",
        playstore_link="https://play.google.com/store/apps/details?id=com.alphaomardiallo.a100_days_of_code"

    )

    app4 = App(
        img_resource="https://play-lh.googleusercontent.com/f8zgttIoxfZb2kkqsZHrx4S92Ky17qOPG3uxPSAnYLcn"
                     "-RoFUMTRJPxxeDomHCSTGck=w480-h960",
        description="Find public wi-fi, toilets and fountains in Paris",
        name="Paris Access",
        playstore_link="https://play.google.com/store/apps/details?id=com.alphaomardiallo.freewifiparis.android"

    )
    return [app3, app4, app2, app1]
