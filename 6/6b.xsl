<?xml version="1.0" encoding="ISO-8859-1" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="document">
<html>
  <body>
    <xsl:apply-templates select="studentlist" />
  </body>
</html>
</xsl:template>

<xsl:key name="student-by-usn" match="student" use="usn" />

<xsl:template match="studentlist">
  <table border="1">
    <xsl:for-each select="key('student-by-usn', '1-800-5623-1234')">
      <tr>
        <td><xsl:value-of select="usn" /></td>
        <td><xsl:value-of select="name" /></td>
        <td><xsl:value-of select="college" /></td>
        <td><xsl:value-of select="branch" /></td>
        <td><xsl:value-of select="joindate" /></td>
        <td><xsl:value-of select="email" /></td>
      </tr>
    </xsl:for-each>
  </table>
</xsl:template>
</xsl:stylesheet>
