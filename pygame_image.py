import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bgf_img = pg.transform.flip(bg_img, True, False)
    kkt_img = pg.image.load("fig/3.png")
    kkt_img = pg.transform.flip(kkt_img, True, False)
    tmr = 0
    kkt_rct = kkt_img.get_rect()
    kkt_rct.center = 300, 200
    while True:
        x = tmr%3200
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-x, 0])
        screen.blit(bgf_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bgf_img, [-x+4800, 0])
         # こうかとんrectの抽出
        
        

        key_lst = pg.key.get_pressed() #全キーの押下状態を取得
        if key_lst[pg.K_UP]:
            kkt_rct.move_ip((0, -1))
        if key_lst[pg.K_DOWN]:
            kkt_rct.move_ip((0, +1))
        if key_lst[pg.K_LEFT]:
            kkt_rct.move_ip((-1, 0))
        if key_lst[pg.K_RIGHT]:
            kkt_rct.move_ip((+1, 0))

        screen.blit(kkt_img, kkt_rct)

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()