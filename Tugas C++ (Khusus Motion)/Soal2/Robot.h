class Robot {
	private:
		int x_now = 0;
		int y_now = 0;
		
	public:
		void printlocation(int x, int y);
		void updatelocation(int x, int y);
		void getlocation();
};
