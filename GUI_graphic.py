import flet as ft


class App:
    def __init__(self,page:ft.Page):
        self.page=page
        self.page.title="Application d'étude"
        self.page.theme_mode=ft.ThemeMode.LIGHT
        
    
    def build(self):
        self.side_content=ft.Column(expand=True)
        self.content=ft.Row(
            expand=True,
            controls=[
                ft.Container(
                    width=400,
                    bgcolor=ft.Colors.BLUE,
                    padding=30,
                    border_radius=20,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content= ft.TextButton(
                                text="Acceuil",
                                icon=ft.Icons.HOME,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE
                                ),
                                on_click=lambda e:self.page_acceuil()
                            ),
                                
                                
                                #0.28.3
                                
                            ),
                            ft.Divider(thickness=5,color=ft.Colors.WHITE),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content= ft.TextButton(
                                text="whatch Video",
                                icon=ft.Icons.VIDEO_CALL,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE
                                ),
                                on_click=lambda e:self.page_video()
                            ),
                                
                                
                                
                                
                            ),
                            ft.Divider(thickness=5,color=ft.Colors.WHITE),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content= ft.TextButton(
                                text="Audio",
                                icon=ft.Icons.AUDIO_FILE,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE
                                ),
                                on_click=lambda e:self.page_audio()
                            ),
                                
                                
                                
                                
                            ),
                            ft.Container(expand=True),
                            ft.Divider(thickness=5,color=ft.Colors.WHITE),
                            ft.Container(
                                alignment=ft.alignment.center,
                                content= ft.TextButton(
                                text="settings",
                                icon=ft.Icons.SETTINGS,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE
                                ),
                                on_click=lambda e:self.settings()
                            ),
                                
                                
                                
                                
                            ),
                            
                        ]
                    ),
                ),
                ft.Container(
                    expand=True,
                    padding=30,
                    content=ft.Column(
                        controls=[
                            self.side_content
                        ]
                    )
                ),
            ] )
        self.page_acceuil()#pour que  la  page d'accceuil s'affiche par defaut
        self.page.add(
            self.content
            
        )
    def page_acceuil(self): 
        self.side_content.controls=[
            #ft.Text(value="La page d'acceuil",size=30,weight=ft.FontWeight.BOLD),
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Row(
                        controls=[
                            ft.Container(width=200),
                            
                            ft.Container(
                                border_radius=100,
                                width=100,
                                height=100,
                                border=ft.border.all(5, ft.Colors.BLUE),
                                content=ft.Image(
                                    src="bdi.png",
                                    fit=ft.ImageFit.FILL
                                )
                        
                            ),
                        
                            
                            
                            
                        ]
                    )           
                                
                                
                
                    ]           
                
            ),
            
            ft.Container(
                            margin=30,
                            border=ft.border.all(20,color=ft.Colors.BLUE),
                            padding=0,
                            height=500,
                            content=ft.Column(
                                controls=[
                                    ft.Container(
                                        height=250,
                                        border=ft.border.only(bottom=ft.BorderSide(10,ft.Colors.BLUE)),
                                        padding=10,
                                        margin=0,
                                        content=ft.Tabs(
                                            selected_index=0,
                                            animation_duration=200,
                                            divider_color=ft.Colors.with_opacity(0.7,ft.Colors.BLUE),
                                            tabs=[
                                                ft.Tab(
                                                    text="acceuil",
                                                    icon=ft.Icons.HOME,
                                                    content=ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    expand=True,
                                                                    scroll=ft.ScrollMode.ADAPTIVE,
                                                                    controls=[
                                                                        ft.Column(
                                                                            expand=True,
                                                                            controls=[
                                                                                ft.Row(
                                                                                    expand=True,
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            width=150,
                                                                                            on_click=lambda e:print(""),
                                                                                            
                                                                                            content=ft.Column(
                                                                                                controls=[
                                                                                                    ft.Icon(name=ft.Icons.DATA_EXPLORATION_OUTLINED,size=40,color=ft.Colors.BLACK),
                                                                                                    ft.Container(
                                                                                                        width=80,
                                                                                                        
                                                                                                        content=ft.Text(value="Obtenir des données ^")
                                                                                                        ),
                                                                                                ]
                                                                                            )
                                                                                            ),
                                                                                        ft.Column(
                                                                                            controls=[
                                                                                                ft.Row(
                                                                                                    controls=[
                                                                                                        ft.Icon(name=ft.Icons.FILE_COPY_OUTLINED),
                                                                                                        ft.Text(value="A partir d'un fichier text ou csv"),
                                                                                                    ]
                                                                                                ),
                                                                                                ft.Row(
                                                                                                    controls=[
                                                                                                        ft.Icon(name=ft.Icons.WEB_ASSET_OFF_OUTLINED),
                                                                                                        ft.Text(value="A partir du web")
                                                                                                    ]
                                                                                                ),
                                                                                                ft.Row(
                                                                                                    controls=[
                                                                                                        ft.Icon(name=ft.Icons.TABLE_BAR_OUTLINED),
                                                                                                        ft.Text(value="A partir du tableau ou d;une plage")
                                                                                                    ]
                                                                                                )
                                                                                            ],
                                                                                            
                                                                                        ),
                                                                                        ft.Column(
                                                                                            controls=[
                                                                                                ft.Row(
                                                                                                controls=[
                                                                                                    ft.Icon(name=ft.Icons.SOURCE_OUTLINED),
                                                                                                    ft.Text(value="Source recente")
                                                                                                ]
                                                                                            ),
                                                                                            ft.Row(
                                                                                                controls=[
                                                                                                    ft.Icon(name=ft.Icons.CONNECT_WITHOUT_CONTACT_SHARP),
                                                                                                    ft.Text(value="Connexion existante")
                                                                                                ]
                                                                                            )
                                                                                            ]
                                                                                        ),
                                                                                    ]
                                                                                ),
                                                                                ft.Row(
                                                                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                                                    controls=[
                                                                                        ft.Container(
                                                                                            height=30,
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.Text(value="Recuperer et transformer les donnees")
                                                                                )
                                                                                    ]
                                                                                )
                                                                                
                                                                            ]
                                                                            ),
                                                                        ft.Container(
                                                                            border=ft.border.only(right=ft.BorderSide(5,ft.Colors.BLACK)),
                                                                            margin=ft.margin.only(top=10,bottom=10),
                                                                        ),
                                                                        ft.Column(
                                                                            expand=True,
                                                                            controls=[
                                                                                ft.Row(
                                                                                    expand=True,
                                                                                    controls=[
                                                                                        ft.Column(
                                                                                            controls=[
                                                                                                ft.Container(
                                                                                                    width=60,
                                                                                                    content=ft.Column(
                                                                                                        controls=[
                                                                                                            ft.Icon(name=ft.Icons.SYSTEM_UPDATE_ALT_OUTLINED,size=20),
                                                                                                            ft.Text(value="Actualiser tout"),
                                                                                                        ]
                                                                                                    )
                                                                                                )
                                                                                            ]
                                                                                        ),
                                                                                        ft.Column()
                                                                                    ]
                                                                                ),
                                                                                ft.Row(),
                                                                                
                                                                                
                                                                            ]
                                                                        ),
                                                                    ]
                                                                )
                                                            ]
                                                        )
                                                    )
                                                ),  ft.Tab(
                                                    text="Video",
                                                    icon=ft.Icons.HOME,
                                                    content=ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(value="video")
                                                            ]
                                                        )
                                                    )
                                                ),  ft.Tab(
                                                    text="audio",
                                                    icon=ft.Icons.HOME,
                                                    content=ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(value="Audio")
                                                            ]
                                                        )
                                                    )
                                                ),  ft.Tab(
                                                    text="Image",
                                                    icon=ft.Icons.HOME,
                                                    content=ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(value="Image")
                                                            ]
                                                        )
                                                    )
                                                ),  ft.Tab(
                                                    text="Settings",
                                                    icon=ft.Icons.HOME,
                                                    content=ft.Container(
                                                        content=ft.Column(
                                                            controls=[
                                                                ft.Text(value="Paramètres")
                                                            ]
                                                        )
                                                    )
                                                ),
                                            ]
                                        )
                                    )
                                ]
                            )
                        ),
        
        ]   
            
        
        
        self.page.update()
    def page_video(self): 
        self.side_content.controls=[
            ft.Text(value="La page de video",size=30,weight=ft.FontWeight.BOLD)
        
        ]  
        self.page.update()
    def page_audio(self): 
        self.side_content.controls=[
            ft.Text(value="La page d'audio",size=30,weight=ft.FontWeight.BOLD,color=ft.Colors.GREEN),
        
        ]  
        self.page.update()
    def settings(self): 
        self.side_content.controls=[
            ft.Text(value="La page de paramtres",size=30,weight=ft.FontWeight.BOLD)
        
        ]  
        self.page.update()
def main(page: ft.Page):
    app=App(page)
    app.build()
    
    
if __name__=="__main__": 
    ft.app(target=main)