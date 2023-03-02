class Robot {
private:
    int x_coord{0}, y_coord{0};

public:
    int* getCoords();                   // Return array containing Robot's latest coords
    void printDirection(int x, int y);  // Print movement direction given x and y shifts
    void updateCoords(int x, int y);    // Update Robot's coords given x and y shifts
};
