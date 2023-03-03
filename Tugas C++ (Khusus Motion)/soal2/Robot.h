class Robot{
    private:
        int absis=0;
        int ordinat=0;

    public:
        Robot()=default;
        Robot(int x, int y) { // Constructor dengan parameter
            absis = x; ordinat = y;
        }
        void arah(int x, int y);//print arah
        void setArah(int x, int y);//set arah
        void akhir();//print koordinat akhir
        void init(); //input
};