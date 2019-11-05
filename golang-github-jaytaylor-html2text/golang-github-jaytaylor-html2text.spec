%global goipath         github.com/jaytaylor/html2text
%global commit          8fb95d837f7d6db1913fecfd7bcc5333e6499596
%global scm             git

%gometa

%global common_description %{expand:
Converts HTML into text of the markdown-flavored variety.
}

%global golicenses      LICENSE
%global godocs          README.md

Name:                   %{goname}
Version:                0
Release:                1%{?dist}
Summary:                Converts HTML into text of the markdown-flavored variety.

License:                MIT
URL:                    %{gourl}
Source0:                %{gosource}


%description
%{common_description}

%gopkg


%prep
%goprep


%install
%gopkginstall


%files
%gopkgfiles



%changelog
* Mon Nov  4 2019 ElXreno <elxreno@gmail.com>
- Initial packaging
