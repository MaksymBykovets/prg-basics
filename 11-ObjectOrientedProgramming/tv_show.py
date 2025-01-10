from tv import TV

def main() : 
    my_TV = TV()

    my_TV.show_status()
    my_TV.turn_on()
    my_TV.show_status()
    my_TV.set_channel(5)
    my_TV.show_status()
    my_TV.turn_off()
    my_TV.show_status()




if __name__ == "__main__" : 
    main()