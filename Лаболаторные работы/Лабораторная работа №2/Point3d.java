public class Point3d{
  // Координата X
  private double xCoord;
  // Координата Y
  private double yCoord;
  // Координата Z
  private double zCoord;

  /** Конструктор инициализации **/
  public Point3d(double x, double y, double z) {
    xCoord = x;
    yCoord = y;
    zCoord = z;
  }

  // Конструктор по умолчанию.
  public Point3d() {
    this(0, 0, 0);
  }

  // Возвращение координаты X 
  public double getX() {
    return xCoord;
  }

  // Возвращение координаты Y 
  public double getY() {
    return yCoord;
  }

  // Возвращение координаты Z
  public double getZ() {
    return zCoord;
  }

  /** Установка значения координаты X. **/
  public void setX(double val) {
    xCoord = val;
  }

  /** Установка значения координаты Y. **/
  public void setY(double val) {
    yCoord = val;
  }

  /** Установка значения координаты Z. **/
  public void setZ(double val) {
    zCoord = val;
  }

  // Сравнение точек: false- точки не равны, true - точки равны
  public boolean compareTo(Point3d p) {
    if((p.getX() == this.getX()) & (p.getY() == this.getY()) & (p.getZ() == this.getZ()))
      return true;
    else
      return false;
  }

  // получение расстояния между точками
  public double distanceTo(Point3d p) {
    double distance = Math.sqrt(
                              Math.pow(p.getX() - this.getX(),2) +
                              Math.pow(p.getY() - this.getY(),2) +
                              Math.pow(p.getZ() - this.getZ(),2));
    return Math.round(distance * 100) / 100.0;
  }
}
