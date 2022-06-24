package com.bigpro.mibird.network.responsemodel
import com.google.gson.annotations.SerializedName

data class Default (
    @SerializedName("namakaryawan")
    var nama_karyawan:String?,
    @SerializedName("tempatlahir")
    var tmp_lhr:String?,
    @SerializedName("tanggallahir")
    var tggl_lhr:String?,
    @SerializedName("bagian")
    var bagian:String?


)